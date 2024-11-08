import os
import sys
import dotenv
import google.generativeai as genai

dotenv.load_dotenv()
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel("gemini-1.5-flash")

file_path = sys.argv[1]

print("Uploading file...")
sample_pdf = genai.upload_file(file_path)
print("File uploaded.")

with open("prompt.txt", "r") as f:
    prompt = f.read()
print("Summarizing...")
response = model.generate_content([prompt, sample_pdf])
print(response.text)
# Save it to markdown
with open("summary.md", "w") as f:
    f.write(response.text)

# Convert markdown to PDF
os.system("mdpdf -o summary.pdf summary.md")