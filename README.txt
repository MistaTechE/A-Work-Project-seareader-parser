RENAISSANCE REPORT PARSER

**STEP 1:**
Download the Renaissance Summary Diagnostic Report.

**STEP 2:**
Double click student_parser and select the report you just downloaded

The following files will be downloaded onto your desktop:

OUTPUT FILES:
- students_30_plus.csv
- students_10_to_29_999.csv

Students with:
• 30.0 or more points → 30_plus file
• 10.0 up to 29.999 → 10_to_29 file
• Below 10 points → Not included







Tech Only (Mac):
To install python: python3 -m pip install pyinstaller
cd /Volumes/NONAME/seareader-parser-master
python3 -m PyInstaller --windowed --onefile student_parser.py


