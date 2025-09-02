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
                - Start message with capital letter.
                - Summarize intent of change in a single line.
                - Be specific~.
                - Do not include file paths or raw diff content.
                - If a TODO comment, message should start with TODO:
                - If change is unclear, fall back to a generic safe message like 'update code', 'add comment', 'remove comment'."""
            },
            {
                "role": "user",
                "content": f"Here is the staged git diff:\n\n{diff}\n\nOnly output the commit message."
            }
        ]
    )
    return chat_completion.choices[0].message.content
