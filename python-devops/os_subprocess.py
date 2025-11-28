import subprocess, os

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def system_info():
    return {"user": os.getlogin(), "cpu": os.cpu_count()}
