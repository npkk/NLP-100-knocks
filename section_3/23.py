import json
from pprint import pprint
import pathlib
import re

IN_FILE = pathlib.Path("output/20.log")
OUT_FILE = pathlib.Path("output/23.log")
Q_STR = r"^=+(?P<section_name>.*)=+$"

matcher = re.compile(Q_STR)

with open(IN_FILE, mode='r') as src, open(OUT_FILE, mode='w') as dst:
    # print(f.read())
    lines = map(lambda s: s.strip('\n'), src.readlines())
    section = list(filter(lambda line: matcher.match(line) is not None, lines))
    section = list(map(lambda line: matcher.match(line).group("section_name"), section))
    section = list(map(lambda name: (name.split("=")[0], len(name.split("="))- 1), section))
    pprint(section, stream=dst)
