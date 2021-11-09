# Import json library
import json

# dict_file for collecting ID and words from txt file
dict_file = {}
# List for collecting dict_file outputs
dict_list = []
# For ID of the dict_file
s = 0
# open txt file to get some data
with open("data/dont_touch.txt", 'r') as file:
    for line in file.readlines():
        dict_file["_id"] = s + 1
        dict_file["word"] = line.rstrip('\n')
        dict_list.append(dict_file)
        s += 1
# Creating and writing json to a new_json.json file
with open("data/new_json.json", 'w') as json_file:
    json.dump(dict_list, json_file, indent=4)