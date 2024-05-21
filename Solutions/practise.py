def min_max(l):
    mini = l[0]
    maxi = l[0]
    for x in range(len(l)):
        if l[x] > maxi:
            maxi = l[x]
        if l[x] < mini:
            mini = l[x]
    print(mini,maxi)

# l = [22, 14, 8, 17, 35, 3,100]
# min_max(l)
def find_k_smallest(l,k):
    for x in range(k):
        posi = x
        for y in range(x+1,len(l)):
            if l[y] < l[posi]:
                posi = y
        l[x],l[posi] = l[posi],l[x]
    print(l[k-1])

# arr = [7,10,4,3,20,15,20]
# k = 3
# find_k_smallest(arr,k)

def sort01(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x] < arr[y]:
                arr[x],arr[y] = arr[y],arr[x]
    print(arr)

# arr = [1,0,0]
# sort01(arr)

def arrangenegative(arr):
    for x in range(len(arr)):
        if arr[x] > 0:
            arr.append(arr[x])
            del arr[x]
    print(arr)


# arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# arrangenegative(arr)
def dounion(arr1,arr2):
    for x in arr1:
        if x not in arr2:
            arr2.append(x)
    print(len(arr2))

# arr1 = [85,25,1,32,54,6]
# arr2 = [85,2]
# dounion(arr1,arr2)

def rotatebyn(arr,n):
    print(arr[0:n] + arr[n:])

# arr1 = [85,25,1,32,54,6]
# n = 2
# rotatebyn(arr1,n)

def maxsubarraysum(nums):
    for x in range(1,len(nums)):
        if nums[x-1] > 0:
            nums[x] += nums[x-1]
    print(max(nums))


# arr = [1, 2, 3, -2, 5]
# maxsubarraysum(arr)

def minitowerheight(arr,k):
    smallest = []
    largest = []
    for x in arr:
        if x - k > 0:
            smallest.append(x-k)
        largest.append((x+k))

    small = min(min(smallest),min(largest))
    large = min(max(smallest),max(largest))
    print(smallest,largest)
    print(small,large)
    print(large-small)

# list_of_values = [1, 5, 8, 10]
# K = 2
# minitowerheight(list_of_values,K)



