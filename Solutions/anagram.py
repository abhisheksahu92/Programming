

def funWithAnagrams(text):
    #Solution 1
    # d = {}
    # for x in text:
    #     temp = ''.join(sorted(x))
    #     if temp not in d.keys():
    #         d[temp] = x
    # print(sorted(d.values()))

    #Solution 2 
    # d = {}
    # a = []
    # for x in text:
    #     s =  ''.join(sorted(list(x)))
    #     if s not in d.keys():
    #         d[s] = ''
    #         a.append(x)
    # a.sort()
    # return a

    #Solution 3
    x = 0
    y = 1
    while True:
        if x < len(text):
            if y < len(text):
                print(text[x],text[y])
                if sorted(text[x]) == sorted(text[y]):
                    text.remove(text[y])
                else:
                    y = y + 1
            else:
                x = x + 1
                y = x + 1
        else:
            print(sorted(text))
            break





if __name__ == '__main__':
    # ['code','aaagmnrs','anagrams','doce'],['poke','pkoe','okpe','ekop']
    list_of_values = [['code','doce','framer','frame'],['code','aaagmnrs','anagrams','doce'],['poke','pkoe','okpe','ekop']]
    
    for li in list_of_values:
        print(f'Input is {li}')
        funWithAnagrams(li)