# Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.
#
# Note: No two strings are the second most repeated, there will be always a single string.

# Input:
# N = 6
# arr[] = {aaa, bbb, ccc, bbb, aaa, aaa}
# Output: bbb
# Explanation: "bbb" is the second most
# occurring string with frequency 2.

def nthrepeatedword(n,words):
    d = {}
    for x in words:
        d[x] = d.get(x,0) + 1
    return sorted(d.items(),key=lambda xy:(xy[1],xy[0]),reverse=True)[n-1][0]

for value in [[2,['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']],[2,['geek', 'for', 'geek', 'for', 'geek', 'aaa']]]:
    print(f'Input is {value}')
    print(nthrepeatedword(*value))