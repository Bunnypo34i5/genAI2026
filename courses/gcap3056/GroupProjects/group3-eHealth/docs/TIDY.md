You are an expert at organizing messy project folders, especially GitHub repositories.

I want to seriously clean up and reorganize my project folder. Please help me create a clear, practical reorganization plan.

My requirements are:
1. Combine similar documents/files into the same folder or merge them if appropriate
   (e.g. multiple similar reports → one folder "Reports", multiple versions of proposal → keep best + archive old)
2. Remove redundant / duplicate / useless files
   (old backups, files with almost identical content, temporary files, .DS_Store, Thumbs.db, very old drafts with no value, etc.)
3. Rename files and folders with clear, consistent, descriptive names so that anyone (including future me) immediately understands the content just from the filename
   → Use kebab-case or snake_case consistently (you choose one style and stick to it)
   → Include dates only when actually useful (e.g. final-report-2025-03.pdf)
   → Avoid vague names like "test", "new", "copy", "final_v2_really_final", "123", etc.
   → Prefer names that answer: What + Purpose + Version/Date (when relevant)

Folder context / current situation:
───────────────────────────────────────────────
Paste here either:

A. A tree-like structure of your current folder
   (you can get it by running:  tree -L 3   or   tree /F   in terminal/cmd)

—or—

B. A list of all important files and folders you currently see, for example:

project-root/
├── meeting_notes_2024.docx
├── meeting notes final.docx
├── proposal v1.pdf
├── proposal-v2-final-really.pdf
├── data_analysis.py
├── data analysis old.py
├── data_analysis_newest.py
├── temp_results.csv
├── results_backup_0301.csv
├── presentation.pptx
├── presentation_final.pptx
├── old_presentation.pptx
├── requirements_old.txt
├── requirements.txt
├── .DS_Store
├── notebook1.ipynb
├── Untitled.ipynb
└── random_stuff/

───────────────────────────────────────────────

Please produce your answer in this exact order and format:

1. Current Problems Summary
   (list the main issues you see: duplicates, inconsistent naming, messy structure, etc.)

2. Proposed New Folder Structure
   (show the full suggested folder tree using text tree format)
   Example:
   project-root/
   ├── docs/
   │   ├── proposals/
   │   ├── reports/
   │   └── meeting-notes/
   ├── src/
   ├── data/
   ├── notebooks/
   └── archive/          ← for safely removed/old stuff

3. File Rename & Action Table
   Use this table format:

   | Current path/filename              | Action              | New path/filename                        | Reason                                      |
   |------------------------------------|---------------------|------------------------------------------|---------------------------------------------|
   | meeting_notes_2024.docx            | rename              | docs/meeting-notes/2024-05-team-sync.md  | clearer name + moved to proper folder       |
   | proposal v1.pdf                    | move to archive     | archive/proposals/proposal-v1-2024.pdf   | superseded by newer version                 |
   | temp_results.csv                   | delete              | —                                        | temporary file, content already in results/ |
   | data_analysis_newest.py            | rename + move       | src/analysis/main_data_processor.py      | descriptive name + proper location          |

4. Files/Folders to DELETE (with strong justification)
   List them separately so I can double-check before actually deleting.

5. Safety Recommendations
   - What should I do first (backup, git commit, etc.)
   - How to handle files I'm unsure about
   - Any git-related advice (e.g. .gitignore updates)

Be conservative about deletions — only strongly recommend deleting clearly useless files.
Aim for clean, professional, maintainable structure suitable for a GitHub repo.

Start now.