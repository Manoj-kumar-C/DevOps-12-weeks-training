import subprocess

def create_venv():
    subprocess.run(["python3", "-m", "venv", "venv"])

def install_requirements():
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
