import tkinter as tk
from tkinter import messagebox
import pdfplumber
import re
import pandas as pd
import os
import sys
from tkinter import filedialog

#BASE_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))
#os.chdir(BASE_DIR)
#PDF_NAME = os.path.join(BASE_DIR, "renaissance_report.pdf")

#def get_base_dir():
    #if getattr(sys, "frozen", False):
        #return os.path.dirname(os.path.dirname(sys.executable))
    #return os.path.dirname(os.path.abspath(__file__))

#BASE_DIR = get_base_dir()
#PDF_NAME = os.path.join(BASE_DIR, "renaissance_report.pdf")

#OUTPUT_DIR = BASE_DIR

OUTPUT_DIR = os.path.expanduser("~/Desktop")

def clean_text(text):
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_students(text):
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
    #if not os.path.exists(PDF_NAME):
        #print(f"\nERROR: '{PDF_NAME}' not found in this folder.")
        #print("Make sure the PDF is saved in the same folder and named correctly.\n")
        #sys.exit(1)
        #messagebox.showerror("Error", "PDF not found")
        #return
    if not os.path.exists(PDF_NAME):
        messagebox.showerror("Error", "Selected PDF could not be found.")
        return


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

    df_30_plus.to_csv(os.path.join(OUTPUT_DIR, "students_30_plus.csv"), index=False)
    df_10_to_29.to_csv(os.path.join(OUTPUT_DIR, "students_10_to_29_999.csv"), index=False)

    messagebox.showinfo(
    "Success",
    "CSV files created on your Desktop!"
    )

# GUI Window
root = tk.Tk()
root.title("Renaissance Report Parser")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, text="Renaissance Report Parser", font=("Arial", 14))
label.pack(pady=15)

def select_pdf_and_run():
    global PDF_NAME

    file_path = filedialog.askopenfilename(
        title="Select Renaissance PDF",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        return

    PDF_NAME = file_path
    main()

#status_label = tk.Label(root, text="Processing report...\nPlease wait.")
status_label = tk.Label(root, text="Select a Renaissance PDF to begin")
status_label.pack(pady=10)
button = tk.Button(root, text="Select PDF", command=select_pdf_and_run)
button.pack(pady=10)
root.mainloop()

#if __name__ == "__main__":
    #main()