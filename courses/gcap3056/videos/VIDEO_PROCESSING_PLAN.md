# Video Processing & Visual Summary Plan
## GCAP 3056 Spring 2026 - Week 1 Video

**Date:** 2026-01-XX  
**Video:** `week 1 video.mp4`  
**Transcript:** `week1GCAP3056.vtt`  
**Duration:** ~1 hour 10 minutes  
**Transcript Lines:** 2,054 lines

---

## Executive Summary

This plan explores options for processing the Week 1 lecture video and creating a visual summary component to display under the embedded video on the course website. The goal is to enhance student engagement and provide quick reference to key topics covered in the lecture.

---

## Part 1: Video vs Script Processing Analysis

### Option A: Process Video Directly
**Pros:**
- Can extract visual elements (slides, screen content, keyframes)
- Can analyze visual cues and transitions
- Can create thumbnail summaries
- More comprehensive content extraction

**Cons:**
- Requires video processing libraries (ffmpeg, opencv, etc.)
- Much larger computational requirements
- Longer processing time
- More complex implementation
- May require video hosting/streaming infrastructure

**Use Cases:**
- Extract keyframes for visual summary
- Create chapter markers based on slide changes
- Generate thumbnail grid
- Extract on-screen text (OCR)

### Option B: Process Script/Transcript Only (RECOMMENDED)
**Pros:**
- ✅ Fast and lightweight processing
- ✅ Already have VTT file with timestamps
- ✅ Easy to parse and analyze
- ✅ Can extract key topics, timestamps, and summaries
- ✅ No video processing overhead
- ✅ Can work with any video hosting (YouTube, Vimeo, self-hosted)
- ✅ Better for text-based search and indexing

**Cons:**
- Cannot extract visual elements
- Misses non-verbal content
- No slide detection

**Use Cases:**
- Extract key topics and timestamps
- Create chapter/topic navigation
- Generate text summary
- Create searchable transcript
- Build topic timeline

### Recommendation: **Process Script Only (Option B)**

**Rationale:**
1. The VTT file already contains structured, timestamped transcript
2. Faster development and deployment
3. Lower resource requirements
4. Can be enhanced later with video processing if needed
5. Works well with existing video embedding (YouTube/iframe)
6. Text-based summaries are more accessible and searchable

---

## Part 2: Visual Summary Component Design

### Component Features

#### 1. **Topic Timeline** (Primary Feature)
- Extract major topics from transcript
- Display as horizontal timeline with clickable segments
- Each segment shows:
  - Topic title
  - Start time
  - Duration
  - Brief description

#### 2. **Key Points Summary**
- Bullet points of main concepts
- Organized by topic
- Clickable to jump to video timestamp

#### 3. **Chapter Navigation**
- Auto-detect topic transitions
- Create chapter markers
- Quick navigation sidebar

#### 4. **Searchable Transcript**
- Full transcript with timestamps
- Search functionality
- Click to jump to video position

#### 5. **Statistics Dashboard**
- Video duration
- Number of topics covered
- Word count
- Speaking pace

### Visual Design Mockup

```
┌─────────────────────────────────────────────────────────┐
│  [Embedded Video Player]                                 │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│  📊 Video Summary                                        │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Timeline: [═══●══════●══════●══════●══════]            │
│            Topic 1  Topic 2  Topic 3  Topic 4           │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │ 📝 Key Topics                                    │   │
│  │ • Course Introduction (00:00 - 02:30)            │   │
│  │ • Code on Access to Information (03:00 - 05:00) │   │
│  │ • Research Methodology (05:00 - 15:00)          │   │
│  │ • Impact Channels (15:00 - 30:00)               │   │
│  └─────────────────────────────────────────────────┘   │
│                                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │ 🔍 Search Transcript                            │   │
│  │ [Search box...]                                 │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## Part 3: Implementation Plan

### Phase 1: Script Processing (Foundation)
**Time Estimate:** 2-3 hours

1. **Parse VTT File**
   - Extract timestamps and text
   - Clean and normalize text
   - Group by time segments

2. **Topic Detection**
   - Use keyword analysis
   - Detect topic transitions
   - Identify major sections

3. **Summary Generation**
   - Extract key sentences
   - Create topic summaries
   - Generate bullet points

**Deliverables:**
- Python script to process VTT
- JSON output with structured data
- Topic extraction algorithm

### Phase 2: React Component Development
**Time Estimate:** 3-4 hours

1. **Create VideoSummary Component**
   - Parse processed data
   - Display timeline
   - Topic navigation

2. **Integration with Week1.tsx**
   - Add component below video
   - Connect to video player
   - Handle timestamp jumps

3. **Styling**
   - Match existing design system
   - Responsive layout
   - Interactive elements

**Deliverables:**
- `VideoSummary.tsx` component
- Updated `Week1.tsx` with integration
- Styled UI matching course website

### Phase 3: Enhanced Features (Optional)
**Time Estimate:** 2-3 hours

1. **Search Functionality**
   - Full-text search in transcript
   - Highlight matches
   - Jump to timestamp

2. **Export Options**
   - Download transcript
   - Print summary
   - Share link with timestamp

3. **Accessibility**
   - Keyboard navigation
   - Screen reader support
   - ARIA labels

---

## Part 4: Technical Stack

### Script Processing
- **Language:** Python
- **Libraries:**
  - `webvtt-py` or custom parser for VTT
  - `nltk` or `spacy` for text analysis (optional)
  - `json` for data output

### Frontend Component
- **Framework:** React (TypeScript)
- **Location:** `Lovable/src/components/features/VideoSummary.tsx`
- **Dependencies:**
  - Existing UI components (Card, Button, etc.)
  - React hooks for state management
  - Video player integration

### Data Format
```json
{
  "videoId": "week1",
  "duration": "01:10:57",
  "topics": [
    {
      "id": 1,
      "title": "Course Introduction",
      "startTime": "00:00:00",
      "endTime": "00:02:30",
      "duration": "02:30",
      "summary": "Introduction to course philosophy...",
      "keyPoints": ["Accountability", "Transparency"]
    }
  ],
  "transcript": [
    {
      "id": 1,
      "startTime": "00:00:00.560",
      "endTime": "00:00:07.030",
      "text": "I record my lessons all the time...",
      "speaker": "classroom"
    }
  ]
}
```

---

## Part 5: Decision Matrix

| Feature | Video Processing | Script Processing | Winner |
|---------|-----------------|-------------------|--------|
| Development Speed | Slow (4-6 hours) | Fast (2-3 hours) | Script |
| Resource Usage | High | Low | Script |
| Visual Content | Yes | No | Video |
| Text Content | Yes | Yes | Tie |
| Searchability | Medium | High | Script |
| Accessibility | Medium | High | Script |
| Maintenance | Complex | Simple | Script |
| Scalability | Limited | High | Script |

**Overall Winner: Script Processing** ✅

---

## Part 6: Next Steps

### Immediate Actions
1. ✅ Create this planning document
2. ⏳ Review and approve approach
3. ⏳ Develop VTT parser script
4. ⏳ Implement topic detection
5. ⏳ Create React component
6. ⏳ Integrate with Week1 page
7. ⏳ Test and refine

### Future Enhancements
- Add video processing for keyframe extraction (if needed)
- Implement AI-powered topic clustering
- Add sentiment analysis
- Create automated chapter generation
- Build analytics dashboard

---

## Part 7: Questions to Consider

1. **Video Hosting:**
   - Where will the video be hosted? (YouTube, Vimeo, self-hosted)
   - Do we need to upload the MP4 file?
   - Should we use existing YouTube embeds?

2. **Video Player:**
   - Use existing iframe approach?
   - Need custom player with timestamp control?
   - Should summary control video playback?

3. **Content Updates:**
   - Will there be more videos to process?
   - Should this be automated?
   - Need batch processing capability?

4. **User Experience:**
   - Should summary be collapsible?
   - Default expanded or collapsed?
   - Mobile-friendly design priority?

---

## Conclusion

**Recommended Approach:** Process the VTT transcript file to create a structured summary component. This approach is:
- ✅ Fast to implement
- ✅ Low resource requirements
- ✅ Highly functional for student needs
- ✅ Easy to maintain and extend

The visual summary will enhance the learning experience by providing:
- Quick topic navigation
- Searchable transcript
- Key points reference
- Time-based chapter markers

**Estimated Total Time:** 5-7 hours for full implementation

---

## Status

- [x] Plan created
- [ ] Plan reviewed
- [ ] Implementation started
- [ ] Testing completed
- [ ] Deployed
