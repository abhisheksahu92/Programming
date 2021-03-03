def maxi(arr):
    max_diff = 0
    for i in range(len(arr)):
        maxi = 0
        mini = 0
        element = arr[i]
        value = abs(len([x for x in arr[i+1:len(arr)] if x < element]) - len([x for x in arr[0:i] if x > element]))
        if max_diff < value:
            max_diff = value

    print(max_diff)

for x in [[1,4,2,7]]:
    maxi(x)