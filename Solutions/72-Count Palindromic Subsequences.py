# Count Palindromic Subsequences

# Given a string str of length N, you have to find number of palindromic subsequence (need not necessarily be distinct) which could be formed from the string str.
# Input:
# Str = "abcd"
# Output:
# 4
# Explanation:
# palindromic subsequence are : "a" ,"b", "c" ,"d"

# Input:
# Str = "aab"
# Output:
# 4
# Explanation:
# palindromic subsequence are :"a", "a", "b", "aa"

def countPs(str1):
    x = 0
    y = 0
    l = []
    while True:
        if x < len(str1):
            if y < len(str1):
                temp = str1[x:y+1]
                if temp == temp[::-1]:
                    l.append(temp)
                y = y + 1
            else:
                x += 1
                y = x
        else:
            break
    return len(l)

for value in ['abcd','aab']:
    print(f'Input is {value}')
    print(countPs(value))