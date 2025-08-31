import os
from groq import Groq

def generate_commit_message(diff):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """You are an assistant that writes clear, concise, and professional 
                Git commit messages based on a provided code diff.
                Guidelines:
                - Summarize the intent of the change in a single line.
                - Keep the message under 70 characters.
                - Do not include file paths or raw diff content.
                - If a TODO comment, the message should start with TODO:
                - Do not use prefixes like 'feat:', 'fix:', 'docs:'.
                - If the change is unclear, fall back to a generic safe message like 'update code'."""
            },
            {
                "role": "user",
                "content": f"Here is the staged git diff:\n\n{diff}\n\nWrite a single commit message. Only output the commit message."
            }
        ]
    )
    return chat_completion.choices[0].message.content
