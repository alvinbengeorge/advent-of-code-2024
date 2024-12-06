import re

with open("input.txt", "r") as f:
    pattern = r"(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, f.read())
    s = 0
    enabled = True
    for e, d, a, b in matches:
        if e:
            enabled = True
        if d:
            enabled = False
        if enabled and a and b:
            s += int(a) * int(b)
    print(s)