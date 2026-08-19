# AI Collaboration Note

**AI Use:**
ChatGPT was used to help write the code, and Claude was used to
summarize and organize documentation.

**How It Was Used:**
ChatGPT wrote the initial version of the parser, including the first
regex pattern. It also helped generate a synthetic PDF report. I 
redacted FERPA-protected information from a real report, and ChatGPT 
recreated a PDF in the same format with synthetic student data.
I used ChatGPT feedback as I modified the code to adjust for issues.

**One Prompt, Workflow, Or Moment That Helped:**
Initially, the tool had a hardcoded PDF filename and file location, 
requiring the user to rename and move their file correctly every time. 
This added unnecessary friction and wasted time. I prompted ChatGPT to 
change the GUI, adding a file picker so the user could select their PDF.

**One Thing I Decided:**
ChatGPT's code included try/except blocks around the parsing logic that
significantly slowed the tool down. I was concerned the user might close
the tool while it was still processing the data due to believing it was 
frozen. I identified the try/except blocks as contributing to the slowdown, 
commented them out, and confirmed the tool ran much faster without them.
