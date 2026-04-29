#add_homeroom.py
import pandas as pd

def load_students(csv1, csv2):
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)
    return pd.concat([df1, df2], ignore_index=True)

def load_teachers(teacher_csv):
    return pd.read_csv(teacher_csv)

def merge_students_with_teachers(students_df, teachers_df):
    merged = pd.merge(
        students_df,
        teachers_df,
        on=["First Name", "Last Name"],
        how="left"
    )
    return merged

def build_final_csv(csv1, csv2, teacher_csv, output_file):
    students = load_students(csv1, csv2)
    teachers = load_teachers(teacher_csv)

    final = merge_students_with_teachers(students, teachers)

    final.to_csv(output_file, index=False)
    print("Created:", output_file)

if __name__ == "__main__":
    build_final_csv(
        "students_30_plus.csv",
        "students_10_to_29_999.csv",
        "homeroom_teachers.csv",
        "students_with_homerooms.csv"
    )