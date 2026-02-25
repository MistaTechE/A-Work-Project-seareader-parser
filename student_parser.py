import pdfplumber
import re
import pandas as pd
import os
import sys

PDF_NAME = "renaissance_report.pdf"

def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# def extract_students(text):
#     # This pattern captures:
#     # Name
#     # Goal %
#     # Actual %
#     # Goal Points (30.0)
#     # Actual Points (53.9, 51.6, etc.)
#
#     pattern = re.findall(
#         r"([A-Za-z,\- ]+?)\s+\d+%\s+\d+%\s+([\d.]+)\s+([\d.]+)",
#         text
#     )
#
#     students = []
#
#     for row in pattern:
#         full_name = row[0].strip()
#         goal_points = float(row[1])
#         actual_points = float(row[2])  # THIS is what we filter on
#
#         # Split Last, First
#         if "," in full_name:
#             last, first = full_name.split(",", 1)
#         else:
#             parts = full_name.split()
#             first = parts[0]
#             last = parts[-1]
#
#         students.append({
#             "First Name": first.strip(),
#             "Last Name": last.strip(),
#             "Actual Points": actual_points
#         })
#
#     return pd.DataFrame(students)
def extract_students(text):

    # Only match names that look like: Last, First
    # pattern = re.findall(
    #     r"([A-Z][a-zA-Z\-']+,\s*[A-Z][a-zA-Z\-']+)"
    #     r"\s+\d+%?\s+\d+%?\s+[\d.]+\s+([\d.]+)",
    #     text
    # )
    # matches a variety of names
    # pattern = re.findall(
    #     r"([A-Z][a-zA-Z\-']+,\s*[A-Z][a-zA-Z\-'\s]+?)"
    #     r"\s+\d+%?\s+\d+%?\s+[\d.]+\s+([\d.]+)",
    #     text
    # )
    # allow hyphen or percent or number
    pattern = re.findall(
        r"([A-Z][a-zA-Z\-']+,\s*[A-Za-z\-'\s]+?)"
        r"\s+(?:\d+%?|-)+"          # first percent or dash
        r"\s+(?:\d+%?|-)+"          # second percent or dash
        r"\s+(?:[\d.]+|-)+"         # goal points or dash
        r"\s+([\d.]+)",             # actual points (we capture this)
        text
    )

    students = []

    for full_name, actual_points in pattern:

        actual_points = float(actual_points)

        last, first = full_name.split(",", 1)

        students.append({
            "First Name": first.strip(),
            "Last Name": last.strip(),
            "Actual Points": actual_points
        })

    return pd.DataFrame(students)

def main():
    if not os.path.exists(PDF_NAME):
        print(f"\nERROR: '{PDF_NAME}' not found in this folder.")
        print("Make sure the PDF is saved in the same folder and named correctly.\n")
        sys.exit(1)

    with pdfplumber.open(PDF_NAME) as pdf:
        full_text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                full_text += page_text + " "

    cleaned = clean_text(full_text)
    df = extract_students(cleaned)

    # Filtering logic
    df_30_plus = df[df["Actual Points"] >= 30.0]
    df_10_to_29 = df[(df["Actual Points"] >= 10.0) & (df["Actual Points"] < 30.0)]

    df_30_plus.to_csv("students_30_plus.csv", index=False)
    df_10_to_29.to_csv("students_10_to_29_999.csv", index=False)

    print("\nSuccess!")
    print("Created:")
    print(" - students_30_plus.csv")
    print(" - students_10_to_29_999.csv\n")

if __name__ == "__main__":
    main()