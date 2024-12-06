import re

with open("input.txt", "r") as f:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, f.read())
    print("All matches:", matches)
    print(sum([int(i) * int(j) for i, j in matches]))