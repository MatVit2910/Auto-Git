import sys
from dotenv import load_dotenv
from git_utils import run_git_command, check_staged_changes, get_staged_diff
from llm_utils import generate_commit_message

load_dotenv()

def main():
    # use command line arguments to change path of working directory if not current
    # example: alias gpush="python auto-git.py /home/user/project"
    if len(sys.argv) > 1:
        repo_path = sys.argv[1]
    else:
        repo_path = None
    things_to_add = input("Add (file/folder or . for everything): ")
    run_git_command(["git", "add", things_to_add], repo_path)
    print("\n")

    if check_staged_changes(repo_path):
        diff = get_staged_diff(repo_path)
        message = generate_commit_message(diff)
        print(f"Generated commit message:\n{message}\n")

        ans = ""
        while ans not in {"y", "n"}:
            ans = input("Continue with commit? (y/n): ").strip().lower()
        if ans == "y":
            run_git_command(["git", "commit", "-m", message], repo_path)
            branch = input("Branch to push (default is main): ").strip()
            if not branch:
                branch = "main"
            ans = ""
            while ans not in {"y", "n"}:
                ans = input(f"Push to {branch}? (y/n): ").strip().lower()
            if ans == "y":
                run_git_command(["git", "push", "origin", branch], repo_path)
    else:
        print("No staged changes to commit.")

if __name__ == "__main__":
    main()
    #testing