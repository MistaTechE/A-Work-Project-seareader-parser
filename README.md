# README.md
**Track Chosen:** B

**What I Built:**
A tool with a Tkinter GUI extracts student data from a PDF
report with a regex, sorts students into two reward tiers based 
on quarterly points, and outputs that data as two csvs.

**Who It Is For:**
A senior K-12 teacher who manages a reading incentive program for
800+ students. Currently they manually copy/paste student data into
a csv to determine which students qualify for tier 1 or 2 rewards. 
The teacher expends 8 hours, quarterly, at the busiest time of the 
quarter, when they are already overwhelmed with work.

**Data:**
A PDF that provides mostly irrelevant data. The only relevant data 
are student names and reading points for the current quarter. 
Synthetic data is shown in Git, student data was only used on local 
machines. No real student data was committed to Git.

**Assumptions:**
- The sample PDF reproduces the standard report
- "Actual Points" is the correct field to sort students
- Dashes (`-`) in a field mean no data, not zero

**Data Issues I Noticed:**
- Some rows had missing percentage fields represented as dashes, breaking the
- initial parsing pattern until handled explicitly
- Name formatting was varied and matching missed valid students
- App was slow and needed adjustment to avoid users viewing it as frozen

**What I Would Do Next With More Time:**
Scrape homerooms to the csvs and generate reward certificates for each student on
the 30+ csv in folders by homeroom.

**Constraints:**
There is no private, confidential, client, employer, or personal data in
this work. The synthetic data is very limited, but easy to reproduce.
Student names and decimal numbers are the only two data points being scraped 
from the pdf. AI tools were used and are documented in the AI_NOTE.md.
