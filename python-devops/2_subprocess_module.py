
import subprocess

subprocess.run(["ls", "-l"])

result = subprocess.run(["df","-h"], capture_output=True, text=True)
print(result.stdout)

script_result = subprocess.run(["bash","deploy.sh"], capture_output=True, text=True)
print(script_result.stdout)
