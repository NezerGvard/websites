import json

def read_json():
    with open(r'mysite\prototype\static\json\user.json', 'r', encoding='utf-8') as f:
        text = json.load(f)
    return text