import sys
import subprocess


# check if file was provided as argument
def main():

    if len(sys.argv) != 2:
        print("Please provide a file as an argument")


filename = sys.argv[1]

# check file extension and call corresponding script
if filename.endswith(".doc"):
    subprocess.call(["doc_script.py", filename])
elif filename.endswith(".docx"):
    subprocess.call(["docx_script.py", filename])
elif filename.endswith(".pdf"):
    subprocess.call(["pdf_script.py", filename])
else:
    print("Unsupported file type")
