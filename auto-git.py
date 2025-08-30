import os
import subprocess
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def git_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Error:", result.stderr)
    return result.stdout.strip()

def get_diff():
    diff = subprocess.run("git diff --cached", shell=True, capture_output=True, text=True).stdout
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
                Git commit messages based on a provided code diff.\\n\\nGuidelines:\\n- Summarize 
                the intent of the change in a single line.\\n- Use the imperative mood (e.g., 
                'fix bug', 'add feature', 'update docs').\\n- If possible, follow the Conventional 
                Commits style: 'feat:', 'fix:', 'docs:', 'refactor:', 'test:', etc.\\n- Keep the 
                message under 70 characters.\\n- Do not include file paths or raw diff content 
                in the commit message.\\n- If the change is unclear, fall back to a generic but 
                safe description like 'update code'.'''
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

git_command("git add .")
diff = get_diff()
message = generate_commit_message(diff)
git_command(f"git commit -m {message}")
branch = input("Branch: ")
git_command(f"git push origin {branch}")