from argparse import ArgumentParser
import csv
import re

parser = ArgumentParser()
parser.add_argument("editorconfig")
parser.add_argument("editorcsvpath")
args = parser.parse_args()

patt = re.compile(r'\[(?P<ext>.*)\]', re.UNICODE)

with open(args.editorconfig, newline="") as editor_file:
    rows = []
    for i, line in enumerate(editor_file.readlines()):
        if line.strip():
            if "root" in line:
                continue
            if "[" in line:
                idx = patt.search(line).group("ext")
            if "=" in line:
                part1, part2 = line.split(" = ")
                rows.append(
                            (idx, 
                             part1.strip(), 
                             part2.strip())
                             
                )

with open(args.editorcsvpath, mode = "wt", newline="") as new_file:
    writer = csv.writer(new_file)
    for row in rows:
        if row:
            writer.writerow(row)