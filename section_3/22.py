import json
from pprint import pprint
import pathlib
import re

IN_FILE = pathlib.Path("output/20.log")
OUT_FILE = pathlib.Path("output/22.log")
Q_STR = r"^\[\[Category:(?P<category_name>.*)\]\]$"

matcher = re.compile(Q_STR)

with open(IN_FILE, mode='r') as src, open(OUT_FILE, mode='w') as dst:
    # print(f.read())
    lines = map(lambda s: s.strip('\n'), src.readlines())
    category = list(filter(lambda line: matcher.match(line) is not None, lines))
    category = list(map(lambda line: matcher.match(line).group("category_name"), category))
    print('\n'.join(category), file=dst)
