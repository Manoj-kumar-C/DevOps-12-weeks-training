import json

class ConfigManager:
    def __init__(self, file):
        self.file = file

    def load(self):
        with open(self.file) as f:
            self.data = json.load(f)
        return self.data

    def update(self, key, value):
        self.data[key] = value

    def save(self):
        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)
