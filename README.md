RENAISSANCE REPORT PARSER

**STEP 1:**
Download the Renaissance report.

**STEP 2:**
Save it in this folder, seareader-parser-master

**STEP 3:**
Rename the file exactly to:

renaissance_report.pdf

**STEP 4:**
Double-click the student_parser app.
**If** clicking the app does not work try this:
**Press:** Command + Space bar
**Type:** Terminal 
**Press:** Enter
**Type:** python3 student_parser.py
**Press:** Enter

OUTPUT FILES:
- students_30_plus.csv
- students_10_to_29_999.csv

Students with:
• 30.0 or more points → 30_plus file
• 10.0 up to 29.999 → 10_to_29 file
• Below 10 points → Not included







Tech Only:
To install python: python3 -m pip install pyinstaller
cd /Volumes/NONAME/seareader-parser-master
python3 -m PyInstaller --windowed --onefile student_parser.py


