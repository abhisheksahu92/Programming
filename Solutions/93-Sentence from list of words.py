# Recursively print all sentences that can be formed from list of word lists
# Given a list of word lists How to print all sentences possible taking one word from a list at a time via recursion?
# Example:
#
# Input: {{"you", "we"},
#         {"have", "are"},
#         {"sleep", "eat", "drink"}}
#
# Output:
#   you have sleep
#   you have eat
#   you have drink
#   you are sleep
#   you are eat
#   you are drink
#   we have sleep
#   we have eat
#   we have drink
#   we are sleep
#   we are eat
#   we are drink

def sentence_from_list(d1,d2,d3):
    x = 0
    y = 0
    z = 0
    while True:
        if x < len(d1):
            if y < len(d2):
                if z < len(d3):
                    print(d1[x],d2[y],d3[z])
                    z += 1
                else:
                    y += 1
                    z = 0
            else:
                x += 1
                y = 0
        else:
            break

for value in [[["you", "we"],["have", "are"],["sleep", "eat", "drink"]]]:
    print(f'Input is {value}')
    sentence_from_list(*value)