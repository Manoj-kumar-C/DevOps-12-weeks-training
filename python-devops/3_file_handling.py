
import json, csv, yaml

# text
with open("data.txt","w") as f:
    f.write("Hello DevOps!\n")

with open("data.txt") as f:
    print(f.read())

# json
data={"name":"manoj","role":"devops"}
with open("config.json","w") as f:
    json.dump(data,f,indent=4)

with open("config.json") as f:
    print(json.load(f))

# csv
with open("users.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["name","role"])
    writer.writerow(["manoj","devops"])

with open("users.csv") as f:
    for row in csv.reader(f):
        print(row)

# yaml
with open("pod.yaml","w") as f:
    yaml.dump({"kind":"Pod","apiVersion":"v1"},f)

with open("pod.yaml") as f:
    print(yaml.safe_load(f))
