# Auto-Git

**Auto-Git** is a Python-based automation tool designed to streamline your development workflow by handling the `git add`, `git commit`, and `git push` cycle in a single command. It includes LLM integration to help generate meaningful commit messages automatically.

## Table of Contents
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)

---

## Features
* **One-Command Workflow**: Stages all changes, commits them, and pushes to your remote branch.
* **AI-Powered Commits**: Utilizes `llm_utils.py` to generate commit messages based on your specific changes.
* **Customizable Paths**: Can be run from any directory by passing a path argument.

## Installation
Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/MatVit2910/Auto-Git.git
cd Auto-Git
pip install -r requirements.txt
```

## Usage
To make the tool accessible from anywhere, set up a terminal alias:

**For Bash/Zsh:**

Add this line to your `.bashrc` or `.zshrc` file:

```bash
alias gpush="python /path/to/your/Auto-Git/auto-git.py"
```

**Running the Script:**

```bash
# In your working directory
gpush

# Or specify a specific directory
gpush path/to/project
```

<img width="1473" height="925" alt="image" src="https://github.com/user-attachments/assets/7ab6c059-2ed8-49ca-8f6c-8c2757075d16" />

