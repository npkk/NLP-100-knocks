import json
from pprint import pprint
import pathlib
import re

IN_FILE = pathlib.Path("output/20.log")
OUT_FILE = pathlib.Path("output/24.log")
Q_STR = r".*ファイル:(?P<file_name>.*\.[a-z]{3})+?"

matcher = re.compile(Q_STR)

with open(IN_FILE, mode='r') as src, open(OUT_FILE, mode='w') as dst:
    # print(f.read())
    lines = map(lambda s: s.strip('\n'), src.readlines())
    media = list(filter(lambda line: matcher.search(line) is not None, lines))
    media = list(map(lambda line: matcher.search(line).group("file_name"), media))
    pprint(media, stream=dst)
    # print(media, file=dst)