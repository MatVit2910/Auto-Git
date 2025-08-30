from setuptools import setup, find_packages

setup(
    name="auto_git_cli",
    version="0.1",
    packages=find_packages(),
    install_requires=["groq", "python-dotenv"],
    entry_points={
        "console_scripts": [
            "gpush=cli:main"
        ]
    },
)
