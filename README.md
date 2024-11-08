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
```bash

## Usage
Run the following command to start the assistant
```bash
python summarize.py {path to the lecture file("lect1.pdf")}
```
This will make summarization in md format and pdf.

## Disclaimer
This is a simple tool and may not work perfectly for all lectures. It is recommended to review the output and make necessary changes.