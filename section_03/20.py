import json
from pprint import pprint

with open("input/jawiki-country.json", mode='r') as src, open("output/20.log", mode='w') as dst:
    # print(f.read())
    lines = src.readlines()
    data = [json.JSONDecoder().raw_decode(line)[0] for line in lines]
    for d in data:
        if d["title"] == "イギリス":
            print(d["text"], file=dst)