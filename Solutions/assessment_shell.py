def solution(S, K):
    # write your code in Python 3.6
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    n = days.index(S) + (K % 7)
    if n < 7:
        return days[n]
    return days[n % 7]

print(solution('Sat',23))

def solution(A, Y):
    maxi = 0
    for i in range(len(A)-Y):
        for j in range(i+Y,len(A)):
            nums = sum(A[i:i+Y])+ sum(A[j:j+Y])
            if nums > maxi:
                maxi = nums
    return maxi

print(solution([1,4,3],1))
print(solution([1,4,3,5,2,9],1))
print(solution([1,4,3,5,2,9],2))
print(solution([0,0],0))