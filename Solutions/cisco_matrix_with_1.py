from usage_deco import *
import numpy as np

def largestArea(samples):
    # Write your code here
    length = len(samples)
    matrix = np.array(samples)
    for size in range(length,0,-1):
        for startRow in range(0,length-size+1):
            for startCol in range(0,length-size+1):
                if 0 not in matrix[startRow:startRow + size, startCol:startCol + size]:
                    return size
    # num = len(samples) + 1
    # for x in range(num,0,-1):
    #     for y in range(0,num-x):
    #         for n in range(0,num-x+1):
    #             l = []
    #             for z in list(map(lambda y: y[n:n+x], samples[y:y + x])):
    #                 l.extend(z)
    #             print(l)
    #             if all(l):
    #                 return
    # return 0

print(largestArea([[1, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 0],[1, 1, 1, 0, 0],[1, 1, 1, 1, 1]]))