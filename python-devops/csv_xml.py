import csv, xml.etree.ElementTree as ET

def read_csv(path):
    with open(path) as f:
        return list(csv.DictReader(f))

def read_xml(path, tag):
    tree = ET.parse(path)
    root = tree.getroot()
    return [elem.text for elem in root.findall(tag)]
