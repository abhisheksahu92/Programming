# Find pivot element in a sorted and rotated array

# Problem Statement – Suppose we have a sorted array, and now we rotate it N times, find the pivot element. The pivot element would be the largest element. Also, can you calculate N?
#
# Clues –
#
#     Solution should be O(log N) in time and O(1) in space.
#     Can you think of  a binary search based solution where you keep comparing the middle element with the last element?
#
# Solution – The pivot element is basically, the largest element in an array. For a sorted and rotated array, it might be somewhere in between. We can solve this in O(log N) time, through a divide-and-conquer approach, which is similar to peak finding algorithm. We will have the lower limit (low) and the upper limit (high) from which we will calculate the ‘mid’.


def pivotelement(arr,low,high):
    mid = (low+high) // 2

    if low == high:
        return arr[low]

    if high < low:
        return arr[0]

    if arr[mid] > arr[mid+1]:
        return arr[mid]

    if arr[mid] > arr[high]:
        next_to = arr[mid+1:high]
    else:
        next_to = arr[low:mid+1]

    return pivotelement(next_to,0,len(next_to)-1)

for value in [[6,7,8,9, 1, 2, 3, 4]]:
    print(f'Input is {value}')
    print(pivotelement(value,0,len(value)-1))