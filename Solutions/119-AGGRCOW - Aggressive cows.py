# AGGRCOW - Aggressive cows

# Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).
#
# His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
# Input
#
# t – the number of test cases, then t test cases follows.
# * Line 1: Two space-separated integers: N and C
# * Lines 2..N+1: Line i+1 contains an integer stall location, xi
# Output
#
# For each test case output one integer: the largest minimum distance.
# Example
#
# Input:
#
# 1
# 5 3
# 1
# 2
# 8
# 4
# 9
#
# Output:
#
# 3
#
# Output details:
#
# FJ can put his 3 cows in the stalls at positions 1, 4 and 8,
# resulting in a minimum distance of 3.

def findminimum(arr,d_max):
    mid = len(d_max) // 2
    count  = 0
    i = 0

    if len(d_max) == 1:
        return d_max[0]

    for y in range(1,len(arr)):
        if (arr[y] - arr[i]) >= d_max[mid]:
            i = y
            count += 1

    if count > 1:
        return findminimum(arr, d_max[mid+1:])
    else:
        return findminimum(arr,d_max[0:mid])


def aggcows(arr,c):
    arr.sort()
    low = 0
    high = arr[-1]
    d_max = list(range(high-low))
    return findminimum(arr,d_max)

for value in [[[1,2,8,4,9],3]]:
    print(f'Input is {value}')
    print(aggcows(*value))
