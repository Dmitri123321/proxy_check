import json


def read_json(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        items = json.load(f)
    return items


def write_json_all(path, items):
    with open(path, 'w', encoding='utf-8-sig') as file:
        json.dump(items, file, indent=4, ensure_ascii=False)
