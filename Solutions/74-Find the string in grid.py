# Find the string in grid

# Given a 2D grid (G[]) of characters and a word(x), find all occurrences of given word in grid. A word can be matched in all 8 directions at any point. Word is said be found in a direction if all characters match in this direction (not in zig-zag form).
#
# The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up, Vertically down and 4 Diagonal directions.

# Input:  G[][] = {"GEEKSFORGEEKS",
#                  "GEEKSQUIZGEEK",
#                  "IDEQAPRACTICE"};
#         x = "GEEKS"
#
# Output: pattern found at 0, 0
#         pattern found at 0, 8
#         pattern found at 1, 0
import re
def countWord(str1,inputt):
    l = []
    # Diagonal Elements
    if len(inputt) >= len(str1):
        l.append(''.join(list(map(lambda x:inputt[x][x],range(len(str1))))))

     # Up-Down elements
    if len(inputt) >= len(str1):
        for y in range(len(inputt[0])):
            l.append(''.join(list(map(lambda x: x[y], inputt))))

    inputt.extend(l)
    for x,y in enumerate(inputt):
        match =  re.finditer(str1,y)
        for m in match:
            print(f'pattern found at {x}, {m.start()}')
    return str1,inputt

for value in [['GEEKS',['GEEKSFORGEEKS','GEEKSQUIZGEEK','IDEQAPRACTICE','IDEQAPRACTICE','IDEQAPRACTICE']]]:
    print(f'Input is {value}')
    print(countWord(*value))