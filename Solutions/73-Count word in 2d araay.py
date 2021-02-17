# Count of number of given string in 2D character array
# Given a 2-Dimensional character array and a string, we need to find the given string in 2-dimensional character array such that individual characters can be present left to right, right to left, top to down or down to top.
# Input : a ={
#             {D,D,D,G,D,D},
#             {B,B,D,E,B,S},
#             {B,S,K,E,B,K},
#             {D,D,D,D,D,E},
#             {D,D,D,D,D,E},
#             {D,D,D,D,D,G}
#            }
#         str= "GEEKS"
# Output :2
#
# Input : a = {
#             {B,B,M,B,B,B},
#             {C,B,A,B,B,B},
#             {I,B,G,B,B,B},
#             {G,B,I,B,B,B},
#             {A,B,C,B,B,B},
#             {M,C,I,G,A,M}
#             }
#         str= "MAGIC"
#
# Output :3

def countword2D(str1,dict1):
    count = 0
    l = []
    for y in range(len(inputt)):
        l.append(''.join(list(map(lambda x:x[y],inputt))))
    dict1.extend(l)
    print(dict1)
    for x in dict1:
        if str1 in x or str1 in x[::-1]:
            print(x)
            count += 1
    return count

# a=[
#     ['D','D','D','G','D','D'],
#     ['B','B','D','E','B','S'],
#     ['B','S','K','E','B','K'],
#     ['D','D','D','D','D','E'],
#     ['D','D','D','D','D','E'],
#     ['D','D','D','D','D','G']
#     ]
needle = "MAGIC"
inputt = ["BBABBM","CBMBBA","IBABBG",
            "GOZBBI","ABBBBC","MCIGAM"]
for value in [[needle,inputt]]:
    print(f'Input is {value}')
    print(countword2D(*value))