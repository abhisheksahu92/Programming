# Rabin-Karp Algorithm for Pattern Searching

# Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
# Examples:
#
# Input:  txt[] = "THIS IS A TEST TEXT"
#         pat[] = "TEST"
# Output: Pattern found at index 10
#
# Input:  txt[] =  "AABAACAADAABAABA"
#         pat[] =  "AABA"
# Output: Pattern found at index 0
#         Pattern found at index 9
#         Pattern found at index 12

def patternSearch(txt,pat):
    length = len(pat)
    for x in range(0,len(txt)-length+1):
        if txt[x:x+length] == pat:
            print(f'Pattern found at index {x}')

for value in [['THIS IS A TEST TEXT','TEST'],['AABAACAADAABAABA','AABA']]:
    print(f'Input is {value}')
    patternSearch(*value)