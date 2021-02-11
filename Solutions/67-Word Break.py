# Word Break
# Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words.

# Example 1:
# Input:
# n = 12
# B = { "i", "like", "sam", "sung", "samsung", "mobile",
# "ice","cream", "icecream", "man", "go", "mango" }
# A = "ilike"
# Output: 1
# Explanation:The string can be segmented as "i like".

# Example 2:
# Input:
# n = 12
# B = { "i", "like", "sam", "sung", "samsung", "mobile",
# "ice","cream", "icecream", "man", "go", "mango" }
# A = "ilikesamsung"
# Output: 1
# Explanation: The string can be segmented as
# "i like samsung" or "i like sam sung".

def wordBreak(str1,list1):
    start = 0
    prove = ''
    for x in range(len(str1)):
        word = str1[start:x+1]
        if word in list1:
            prove += word
            start = x + 1
    return 1 if prove == str1 else 0
values = [
    ['ilik',['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']],
    ['ilikesamsung',["i", "like", "sam", "sung", "samsung", "mobile","ice","cream", "icecream", "man", "go", "mango" ]]
]
for value in values:
    print(f'Input is {value}')
    print(wordBreak(*value))