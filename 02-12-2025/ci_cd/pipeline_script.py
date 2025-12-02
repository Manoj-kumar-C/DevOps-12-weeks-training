import subprocess, os

def sh(cmd):
    print(">>>", cmd)
    subprocess.run(cmd, shell=True, check=True)

if not os.path.exists(".venv"):
    sh("python3 -m venv .venv")

sh(".venv/bin/pip install -r venv_demo/requirements.txt")
sh(".venv/bin/pytest -q")
print("Pipeline complete.")
