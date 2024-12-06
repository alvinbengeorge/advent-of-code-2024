import time

def getResult(a: list, isRemoved: bool = False):
    isIncreasing = None
    # print(a)
    for i in range(len(a)-1):
        if i==0:
            isIncreasing = (a[i+1] - a[i] > 0)
        if any([
            not (-3 <= a[i+1] - a[i] <= 3),
            a[i+1] - a[i] <= 0 and isIncreasing,
            a[i+1] - a[i] >= 0 and not isIncreasing
        ]): 
            if not isRemoved:
                for i in range(len(a)):
                    a_copy = a.copy()                    
                    a_copy.pop(i)
                    print(a_copy)
                    if getResult(a_copy, True):
                        return True
            return False
    return True

text = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

start = time.time()
with open("input.txt", "r") as f:
    count=0
    for a in f.readlines():
        if not a: continue
        if (getResult([int(i) for i in a.split(' ')])):
            count+=1
    print(count)
end = time.time()

print(end-start)
