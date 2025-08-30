import os
import subprocess
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def git_command(command):
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
    return result.stdout.strip()

def check_staged_changes():
    result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    return result.returncode != 0

def get_diff():
    diff = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True).stdout
    return diff

def generate_commit_message(diff):
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
             {
                "role": "system",
                "content": '''You are an assistant that writes clear, concise, and professional 
                Git commit messages based on a provided code diff.\n\nGuidelines:\n- Summarize 
                the intent of the change in a single line.\n- Keep the message under 70 characters.
                \n- Do not include file paths or raw diff content in the commit message.\n- Do not 
                use prefixes like 'feat:', 'fix:', 'docs:'.\n- If the change is unclear, fall back 
                to a generic but safe description like 'update code'.'''
            },
            {
                "role": "user",
                "content": f'''Here is the staged git diff:\\n\\n{diff}\\n\\nWrite a single
                commit message that describes these changes. Follow the system rules strictly. Only 
                output the commit message, nothing else.''',
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=0
    )
    return chat_completion.choices[0].message.content

things_to_add = input("Add: ")
print(f"Running: git add {things_to_add}")
git_command(["git", "add", f"{things_to_add}"])
print("\n")

if check_staged_changes():
    diff = get_diff()
    message = generate_commit_message(diff)
    print(f"Message will be: {message}")
    cont = ""
    while cont != "y" and cont != "n":
        cont = input("Continue? (y/n) ")
    if cont == "y":
        git_command(["git", "commit", "-m", f"\"{message}\""])
        branch = input("Branch: ")
        print(f"Pushing from origin to {branch}")
        cont = ""
        while cont != "y" and cont != "n":
            cont = input("Continue? (y/n) ")
        if cont == "y":
            git_command(["git", "push", "origin", f"{branch}"])
else:
    print("No changes to commit")