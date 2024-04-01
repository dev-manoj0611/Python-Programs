list1 = [29, 88, 37, 83, 44, 77]
mini = list1[0]
i = 1
while i in range(list1[i], list1[len(list1)-1]):
    if mini < i:
        i = mini
    else:
        mini = mini
    i += 1
print(mini,'is the smallest element in list1')
