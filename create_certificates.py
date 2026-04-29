#create_certificates.py
import os
from docxtpl import DocxTemplate
from docx2pdf import convert

OUTPUT_DIR = "certificates"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TEMPLATE_FILE = "SY24-25 Jr. SeaREAder Certificate Template.docx"

def generate_certificates(students):
    for student in students:
        name = student["name"]
        points = student["Actual Points"] if "Actual Points" in student else student["points"]

        # Load Word template
        doc = DocxTemplate(TEMPLATE_FILE)

        # Fill placeholders (must match your Word doc exactly)
        doc.render({
            "name": name,
            "points": points
        })

        safe_name = name.replace(" ", "_").replace("/", "-")

        docx_path = os.path.join(OUTPUT_DIR, f"{safe_name}.docx")
        pdf_path = os.path.join(OUTPUT_DIR, f"{safe_name}.pdf")

        doc.save(docx_path)

        # Convert to PDF
        convert(docx_path, pdf_path)

        # Optional cleanup
        os.remove(docx_path)

    print("Certificates generated successfully!")