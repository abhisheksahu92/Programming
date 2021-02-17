# Boyer Moore Algorithm for Pattern Searching

# Pattern searching is an important problem in computer science. When we do search for a string in notepad/word file or browser or database, pattern searching algorithms are used to show the search results. A typical problem statement would be-
# Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
#
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

def patternMatch(txt,pat):
    for x in range(len(txt)):
        if txt[x] == pat[0]:
            if txt[x:x+len(pat)] == pat:
                print(f'Pattern found at index {x}')

for value in [['AABAACAADAABAABA','AABA'],['THIS IS A TEST TEXT','TEST']]:
    print(f'Input is {value}')
    patternMatch(*value)