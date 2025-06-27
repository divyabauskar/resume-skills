import fitz  # PyMuPDF


skills_list = [
    "python", "c", "java", "full stack", "html and css", "html", "c++",
    "django", "flask", "javascript", "excel", "project management", "sql"
]

def extract_skills_from_resume(pdf_path):
    try:
       
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        
        text = text.lower()

        
        skill_counts = {}
        for skill in skills_list:
            count = text.count(skill.lower())
            if count > 0:
                skill_counts[skill] = count

        
        if skill_counts:
            print("\n✅ Skills found in the resume:\n")
            for skill, count in skill_counts.items():
                print(f"• {skill} (mentioned {count} time(s))")
        else:
            print("\n❌ No matching skills found in the resume.")


        missing_skills = [skill for skill in skills_list if skill not in skill_counts]
        if missing_skills:
            print("\n💡 Suggested improvements: Consider adding these skills to your resume:")
            for skill in missing_skills:
                print(f"- {skill}")

    except Exception as e:
        print("\n❌ Error reading the file. Make sure the path and format are correct.")
        print("Details:", e)


pdf_file = input("📄 Enter the PDF file name (with extension or full path): ")
extract_skills_from_resume(pdf_file)
