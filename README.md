# Auto-Git

**Auto-Git** is a Python-based automation tool designed to streamline your development workflow by handling the `git add`, `git commit`, and `git push` cycle in a single command. It includes LLM integration to help generate meaningful commit messages automatically.

## Table of Contents
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [Project Structure](#project-structure)
* [Contact](#contact)

---

## Features
* **One-Command Workflow**: Stages all changes, commits them, and pushes to your remote branch.
* **AI-Powered Commits**: Utilizes `llm_utils.py` to generate commit messages based on your specific changes.
* **Customizable Paths**: Can be run from any directory by passing a path argument.

## Installation
Clone the repository and install the necessary dependencies:

```bash
git clone [https://github.com/MatVit2910/Auto-Git.git](https://github.com/MatVit2910/Auto-Git.git)
cd Auto-Git
pip install -r requirements.txt
