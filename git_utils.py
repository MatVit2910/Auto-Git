import subprocess

def run_git_command(cmd, repo_path=None):
    result = subprocess.run(
        cmd,
        cwd=repo_path,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("Error:", result.stderr)
    return result.stdout.strip()

def check_staged_changes(repo_path=None):
    result = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        cwd=repo_path
    )
    return result.returncode != 0

