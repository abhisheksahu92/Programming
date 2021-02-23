# Write a program to reverse an array or string

# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

def reverse(array):
    return array[::-1]

if __name__ == '__main__':
    print(reverse([1,2,3]))