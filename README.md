# CSED Study Assistant
## Intro
This is a simple assistant for CSED students to help them with their studies. It is a simple command line tool that can be used to summarize lectures

## Installation
1. Clone the repository
2. Run the following command to install the required packages
```bash
pip install -r requirements.txt
```
3. Add gemini api key to `.env`, you can get free api key from [Gemini Studio](https://aistudio.google.com/app/apikey)

## Usage
- Run the following command to start the assistant
```bash
python summarize.py {path to the lecture file("lect1.pdf")}
```
This will make summarization in md format and pdf.

- You can add your own **edits** to markdown file and export it as pdf using command:
```bash
mdpdf -o summary.pdf summary.md
```

- You can add your own prompt by editing `prompt.txt`

## Testing
You can find test results in `test/`

## Future Work
- Adding Web interface for chatting and uploading documents
- Follow up questions on the uploaded document for more clarifications
- Follow up editing requests

## Contribution
You are highly encouraged to fork the repo and make pull requests with new features

## Disclaimer
This is a simple tool and may not work perfectly for all documents. It is recommended to review the output and make necessary changes.

**Enjoy!**
