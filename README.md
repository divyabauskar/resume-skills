🧠 Resume Skill Extractor (Python CLI Tool)
This is a simple Python command-line tool that takes a `.pdf` resume as input and:
✅ Extracts the text  
✅ Counts how many times key skills are mentioned  
✅ Suggests improvements based on missing skills
It uses the `PyMuPDF` library (`fitz`) for PDF text extraction.
🔧 Requirements
- Python 3.7 or higher
- PyMuPDF
Install the required package using:
```bash
pip install PyMuPDF
python skill_extractor.py
📄 Enter the PDF file name (with extension or full path): resume.pdf
What it does
Extracts text from the given PDF file
Searches for a predefined list of common tech and soft skills
Counts how many times each skill appears
Displays the found skills and their counts
Suggests missing skills to consider adding
Sample output:
📄 Enter the PDF file name (with extension or full path): resume.pdf
✅ Skills found in the resume:
• python (mentioned 2 time(s))
• html (mentioned 1 time(s))
💡 Suggested improvements: Consider adding these skills to your resume:
- sql
- flask
- project management
 Made By
Divya Bauskar
Hackweek 2025 Participant
Python enthusiast 🌸 | Learning by building
