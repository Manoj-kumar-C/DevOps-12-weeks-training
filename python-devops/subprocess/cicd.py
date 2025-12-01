import subprocess, os, requests

def trigger_jenkins(url, user, password):
    return requests.post(url, auth=(user, password)).status_code

def terraform_apply():
    subprocess.run(["terraform", "init"])
    subprocess.run(["terraform", "apply", "-auto-approve"])

def git_auto_push(msg="Automated update"):
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", msg])
    subprocess.run(["git", "push", "origin", "master"])


if __name__ == "__main__":
    git_auto_push()

