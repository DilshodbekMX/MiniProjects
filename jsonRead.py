import json

with open('data/new_json.json') as json_file:
    data = json.load(json_file)
    for element in data:
        print(f"ID: {element['_id']}\nWORD: {element['word']}")
