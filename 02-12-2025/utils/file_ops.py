import os, shutil

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def copy_file(src, dest):
    os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
    shutil.copy(src, dest)

def list_files(directory):
    return os.listdir(directory)
