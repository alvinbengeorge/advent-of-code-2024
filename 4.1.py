from typing import List

# row -> text[]
# column -> text[0][]

text = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".split("\n")
text = [list(i) for i in text if i]

def safeCheck(text: List[List[int]], row: int, column: int):
    total = 0
    try:
        # horizontal right
        if (0 <= row < len(text) and 0 <= column < len(text[0]) and 0 <= column+4 < len(text[0])):
            if text[row][column:column+4] == list("XMAS"):
                print("1ST CONDITION", text[row][column:column+4])
                total += 1

        # horizontal left
        if (0 <= row < len(text) and 0 <= column < len(text[0]) and 0 <= column-4 < len(text[0])):
            if text[row][column-3:column+1] == list("XMAS")[::-1]:
                print("2ND CONDITION", text[row][column-3:column+1])
                total += 1  
        
        #vertical down
        if (0 <= row < len(text) and 0 <= row+4 < len(text) and 0 <= column-4 < len(text[0])):
            if [i[column] for i in text[row:row+4]] == list("XMAS"):
                print("3RD CONDITION", [i[column] for i in text[row:row+4]])
                total += 1

        #vertical up
        if (0 <= row < len(text) and 0 <= row-4 < len(text) and 0 <= column-4 < len(text[0])):
            if [i[column] for i in text[row-3:row+1]] == list("XMAS")[::-1]:
                print("4TH CONDITION", [i[column] for i in text[row-3:row+1]])
                total += 1

        #diagonal left top
        if (0 <= row < len(text) and 0 <= row-4 < len(text) and 0 <= column < len(text[0]) and 0 <= column-4 < len(text[0])):
            if [text[row+i][column+i] for i in range(-3, 1)] == list("XMAS")[::-1]:
                print("5TH CONDITION", [text[row+i][column+i] for i in range(-3, 1)])
                total += 1

        #diagonal left bottom
        if (0 <= row < len(text) and 0 <= row+4 < len(text) and 0 <= column < len(text[0]) and 0 <= column-4 < len(text[0])):
            if [text[row-i][column+i] for i in range(-3, 1)] == list("XMAS")[::-1]:                
                print("6TH CONDITION", [text[row-i][column+i] for i in range(-3, 1)])
                total += 1

        #diagonal right top
        if (0 <= row < len(text) and 0 <= row-4 < len(text) and 0 <= column < len(text[0]) and 0 <= column+4 < len(text[0])):
            if [text[row+i][column-i] for i in range(-3, 1)] == list("XMAS"):
                print("7TH CONDITION", [text[row+i][column-i] for i in range(-3, 1)])
                total += 1

        #diagonal right bottom
        if (0 <= row < len(text) and 0 <= row+4 < len(text) and 0 <= column < len(text[0]) and 0 <= column+4 < len(text[0])):
            if [text[row+i][column+i] for i in range(-3, 1)] == list("XMAS"):
                print("8TH CONDITION", [text[row+i][column+i] for i in range(-3, 1)])
                total += 1
    except Exception as e:
        print(row, row-4, row+4, column)
        raise e

    
    return total

a = []
total = 0
for i in range(len(text)):    
    print(i, "|", end=" ")
    a.append([])
    for j in range(len(text[0])):
        a[i].append(safeCheck(text, row=i, column=j) if text[i][j] == 'X' else 0)
        total += a[i][j]
    print()
    
print()

li = ["".join(i) for i in text]
for index, element in enumerate(li):
    print(index, "|", element)

print()

for i in range(len(text)):
    print(i, "|", end=" ")
    for j in range(len(text[0])):
        print(a[i][j], end="")
    print()

print(total)
