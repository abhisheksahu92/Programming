# Smallest window in a string containing all the characters of another string
# Given two strings S and P. Find the smallest window in the S consisting of all the characters of P.
#
# Example 1:
#
# Input:
# S = "timetopractice"
# P = "toc"
# Output:
# toprac
# Explanation: "toprac" is the smallest
# substring in which "toc" can be found.

# Example 2:
#
# Input:
# S = "zoomlazapzo"
# P = "oza"
# Output:
# apzo
# Explanation: "apzo" is the smallest
# substring in which "oza" can be found.

def smallestWindow(str1,str2):
    x = 0
    y = len(str1)
    l = str1
    while True:
        if x < len(str1):
            if y > x:
                if all(list(map(lambda n: n in str1[x:y], str2))):
                    if len(str1[x:y]) < len(l):
                        l = str1[x:y]
                y = y - 1
            else:
                x = x + 1
                y = len(str1)
        else:
            break
    return l

for value in [['timetopractice','toc'],['zoomlazapzo','oza']]:
    print(f'Input is {value}')
    print(smallestWindow(*value))