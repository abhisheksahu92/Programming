# Bishu and Soldiers

# Problem
#
# Bishu went to fight for Coding Club. There were N soldiers with various powers. There will be Q rounds to fight and in each round Bishu's power will be varied. With power M, Bishu can kill all the soldiers whose power is less than or equal to M(<=M). After each round, All the soldiers who are dead in previous round will reborn.Such that in each round there will be N soldiers to fight. As Bishu is weak in mathematics, help him to count the number of soldiers that he can kill in each round and total sum of their powers.
#
# 1<=N<=10000
#
# 1<=power of each soldier<=100
#
# 1<=Q<=10000
#
# 1<=power of bishu<=100

# Sample Input
#
# 7
# 1 2 3 4 5 6 7
# 3
# 3
# 10
# 2

# Sample Output
#
# 3 6
# 7 28
# 2 3

def bishu_and_soldiers(solders,power):
    solders = list(map(int,solders.split()))
    power = list(map(int,power.split()))
    count = 0
    sum1 = 0
    for x in power:
        for y in solders:
            if y <= x:
                count += 1
                sum1 += y
        print(count,sum1)
        count = 0
        sum1 = 0

for value in [['1 2 3 4 5 6 7','3 3 10 2']]:
    print(f'Input is {value}')
    bishu_and_soldiers(*value)