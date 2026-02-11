#!/usr/bin/env python3
"""
Process VTT transcript file and extract topics, summaries, and structured data.
"""

import re
import json
from datetime import datetime, timedelta
from typing import List, Dict, Tuple

def parse_timestamp(ts: str) -> float:
    """Convert VTT timestamp to seconds."""
    parts = ts.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = float(parts[2])
    return hours * 3600 + minutes * 60 + seconds

def format_timestamp(seconds: float) -> str:
    """Convert seconds to HH:MM:SS format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"

def parse_vtt(file_path: str) -> List[Dict]:
    """Parse VTT file and return list of transcript entries."""
    entries = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by double newlines to get cue blocks
    blocks = content.split('\n\n')
    
    for block in blocks:
        block = block.strip()
        if not block or block == 'WEBVTT':
            continue
        
        lines = block.split('\n')
        if len(lines) < 2:
            continue
        
        # Try to find timestamp line
        timestamp_match = None
        text_lines = []
        
        for i, line in enumerate(lines):
            # Match timestamp pattern: 00:00:00.000 --> 00:00:00.000
            match = re.match(r'(\d{2}:\d{2}:\d{2}\.\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}\.\d{3})', line)
            if match:
                timestamp_match = match
                # Text is everything after the timestamp line
                text_lines = lines[i+1:]
                break
        
        if timestamp_match and text_lines:
            start_time = parse_timestamp(timestamp_match.group(1))
            end_time = parse_timestamp(timestamp_match.group(2))
            text = ' '.join(text_lines).strip()
            
            # Remove speaker label if present
            text = re.sub(r'^(classroom|Audio shared by classroom):\s*', '', text, flags=re.IGNORECASE)
            
            if text:
                entries.append({
                    'startTime': start_time,
                    'endTime': end_time,
                    'startTimeFormatted': format_timestamp(start_time),
                    'endTimeFormatted': format_timestamp(end_time),
                    'text': text,
                    'duration': end_time - start_time
                })
    
    return entries

def detect_topics(entries: List[Dict]) -> List[Dict]:
    """Detect major topics from transcript entries."""
    
    # Topic keywords and patterns
    topic_patterns = [
        {
            'title': 'Course Introduction',
            'keywords': ['course about', 'what is this course', 'taking a stand', 'policy recommendations', 
                        'course philosophy', 'accountability', 'transparency'],
            'start_keywords': ['what is this course', 'course about', 'taking a stand'],
        },
        {
            'title': 'Code on Access to Information',
            'keywords': ['code on access to information', 'access to information', 'secret weapon', 
                        'www.access.gov.hk', 'write letters to the government', '21 days'],
            'start_keywords': ['code of access to information', 'secret weapon', 'access to information'],
        },
        {
            'title': 'Letters to the Editor (SCMP)',
            'keywords': ['letters to the editor', 'south china morning post', 'scmp', 'write letters',
                        'published letters', 'mark peeker', '120th anniversary'],
            'start_keywords': ['write letters to the editor', 'south china morning post', 'letters'],
        },
        {
            'title': 'Course Methodology & Impact Channels',
            'keywords': ['research', 'argue', 'impact', 'legislative council', 'legco', 'lawmakers',
                        'media', 'public conversation', 'government response'],
            'start_keywords': ['how can we make sure', 'next step', 'impact channels'],
        },
        {
            'title': 'Course Awards & Recognition',
            'keywords': ['award', 'award-winning', 'ge teaching award', 'general education'],
            'start_keywords': ['award', 'award-winning'],
        },
        {
            'title': 'Student Projects & Examples',
            'keywords': ['student', 'project', 'team', 'lgbt', 'emergency alert', 'national security',
                        'weather', 'chinese medicine', 'emission'],
            'start_keywords': ['student project', 'team project'],
        },
        {
            'title': 'Q&A and Wrap-up',
            'keywords': ['question', 'any questions', 'next week', 'see you', 'enrollment', 'minimum requirement'],
            'start_keywords': ['any questions', 'next week', 'see you'],
        },
    ]
    
    topics = []
    current_topic = None
    topic_start_time = None
    topic_entries = []
    
    for entry in entries:
        text_lower = entry['text'].lower()
        
        # Check if this entry starts a new topic
        new_topic = None
        for pattern in topic_patterns:
            # Check start keywords first (higher priority)
            for keyword in pattern.get('start_keywords', []):
                if keyword.lower() in text_lower:
                    new_topic = pattern
                    break
            if new_topic:
                break
            
            # If no start keyword match, check regular keywords
            if not new_topic:
                for keyword in pattern['keywords']:
                    if keyword.lower() in text_lower:
                        # Only start new topic if we don't have one or it's been a while
                        if not current_topic or entry['startTime'] - topic_start_time > 300:  # 5 minutes gap
                            new_topic = pattern
                            break
                if new_topic:
                    break
        
        # If we found a new topic, finalize the previous one
        if new_topic and (not current_topic or new_topic['title'] != current_topic['title']):
            if current_topic and topic_entries:
                # Create summary for previous topic
                topic_text = ' '.join([e['text'] for e in topic_entries[:10]])  # First 10 entries
                summary = generate_summary(topic_text, current_topic['title'])
                key_points = extract_key_points(topic_entries)
                
                topics.append({
                    'id': len(topics) + 1,
                    'title': current_topic['title'],
                    'startTime': format_timestamp(topic_start_time),
                    'endTime': format_timestamp(topic_entries[-1]['endTime']),
                    'startTimeSeconds': topic_start_time,
                    'endTimeSeconds': topic_entries[-1]['endTime'],
                    'duration': format_duration(topic_entries[-1]['endTime'] - topic_start_time),
                    'summary': summary,
                    'keyPoints': key_points,
                    'entryCount': len(topic_entries)
                })
            
            # Start new topic
            current_topic = new_topic
            topic_start_time = entry['startTime']
            topic_entries = [entry]
        else:
            # Continue current topic
            if current_topic:
                topic_entries.append(entry)
            elif not current_topic:
                # No topic yet, start with first one
                current_topic = topic_patterns[0]
                topic_start_time = entry['startTime']
                topic_entries = [entry]
    
    # Finalize last topic
    if current_topic and topic_entries:
        topic_text = ' '.join([e['text'] for e in topic_entries[:10]])
        summary = generate_summary(topic_text, current_topic['title'])
        key_points = extract_key_points(topic_entries)
        
        topics.append({
            'id': len(topics) + 1,
            'title': current_topic['title'],
            'startTime': format_timestamp(topic_start_time),
            'endTime': format_timestamp(topic_entries[-1]['endTime']),
            'startTimeSeconds': topic_start_time,
            'endTimeSeconds': topic_entries[-1]['endTime'],
            'duration': format_duration(topic_entries[-1]['endTime'] - topic_start_time),
            'summary': summary,
            'keyPoints': key_points,
            'entryCount': len(topic_entries)
        })
    
    return topics

def generate_summary(text: str, title: str) -> str:
    """Generate a brief summary from text."""
    # Simple extraction: take first 2-3 sentences or first 200 chars
    sentences = re.split(r'[.!?]+', text)
    summary_sentences = []
    char_count = 0
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and len(sentence) > 20:
            summary_sentences.append(sentence)
            char_count += len(sentence)
            if len(summary_sentences) >= 2 or char_count > 200:
                break
    
    summary = '. '.join(summary_sentences)
    if summary and not summary.endswith('.'):
        summary += '.'
    
    return summary[:300] if summary else f"Discussion about {title.lower()}."

def extract_key_points(entries: List[Dict], max_points: int = 5) -> List[str]:
    """Extract key points from entries."""
    # Look for sentences with important keywords
    important_keywords = ['important', 'key', 'main', 'essential', 'must', 'should', 'need', 
                         'because', 'therefore', 'however', 'but', 'also']
    
    key_points = []
    all_text = ' '.join([e['text'] for e in entries])
    sentences = re.split(r'[.!?]+', all_text)
    
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 30 and len(sentence) < 200:
            sentence_lower = sentence.lower()
            # Check if sentence contains important keywords or is a definition
            if any(kw in sentence_lower for kw in important_keywords) or 'is' in sentence_lower[:50]:
                # Clean up the sentence
                sentence = re.sub(r'\s+', ' ', sentence)
                if sentence not in key_points:
                    key_points.append(sentence)
                    if len(key_points) >= max_points:
                        break
    
    # If we don't have enough, add some representative sentences
    if len(key_points) < max_points:
        for sentence in sentences:
            sentence = sentence.strip()
            if 50 < len(sentence) < 150 and sentence not in key_points:
                key_points.append(sentence)
                if len(key_points) >= max_points:
                    break
    
    return key_points[:max_points]

def format_duration(seconds: float) -> str:
    """Format duration as MM:SS or HH:MM:SS."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

def main():
    vtt_file = 'week1GCAP3056.vtt'
    output_file = 'week1_video_data.json'
    
    print(f"Processing {vtt_file}...")
    
    # Parse VTT file
    entries = parse_vtt(vtt_file)
    print(f"Parsed {len(entries)} transcript entries")
    
    # Detect topics
    topics = detect_topics(entries)
    print(f"Detected {len(topics)} major topics")
    
    # Calculate total duration
    if entries:
        total_duration = entries[-1]['endTime']
        duration_formatted = format_timestamp(total_duration)
    else:
        total_duration = 0
        duration_formatted = "00:00:00"
    
    # Create output structure
    output = {
        'videoId': 'week1',
        'title': 'Week 1: Understanding Our Mission',
        'duration': duration_formatted,
        'durationSeconds': total_duration,
        'totalEntries': len(entries),
        'topics': topics,
        'transcript': entries[:100]  # Include first 100 entries for preview
    }
    
    # Write to JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Processing complete!")
    print(f"📄 Output saved to: {output_file}")
    print(f"📊 Topics detected: {len(topics)}")
    print(f"⏱️  Total duration: {duration_formatted}")
    
    # Print topic summary
    print("\n📋 Topics:")
    for topic in topics:
        print(f"  {topic['id']}. {topic['title']} ({topic['startTime']} - {topic['endTime']}, {topic['duration']})")

if __name__ == '__main__':
    main()
