text = """
3   4
4   3
2   5
1   3
3   9
3   3
"""
with open("input.txt", "r") as f:
    x, y = [], []
    for i in f.readlines():
        if not i: continue
        a, b = i.split("   ")
        x.append(int(a))
        y.append(int(b))
    x.sort()
    y.sort()
    diff = [abs(x[i] * y.count(x[i])) for i in range(len(x))]
    print(diff)
    print(sum(diff))
