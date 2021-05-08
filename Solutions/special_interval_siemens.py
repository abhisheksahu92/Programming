def Special_Interval (nonspecial, special):
    # Write your code here
    li = []
    for x in nonspecial:
        count = 0
        for y in special:
            if x[0] <= y[1]:
                count += 1
        li.append(count)
    return li

print(Special_Interval([[1, 3], [3, 3], [6, 7]],[[1, 2], [1, 5], [1, 7]]))