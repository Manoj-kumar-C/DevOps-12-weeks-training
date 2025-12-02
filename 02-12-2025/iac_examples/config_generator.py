import json, os

def generate(env):
    cfg = { "env": env, "replicas": 3 if env == "prod" else 1 }
    os.makedirs(f"deploy/{env}", exist_ok=True)
    with open(f"deploy/{env}/config.json", "w") as f:
        json.dump(cfg, f, indent=2)

generate("dev")
generate("prod")
