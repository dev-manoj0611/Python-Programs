list1 = [100, 70, 3, 20, 8, 9, 10]
for i in range(len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[j] > list1[i]:
            var = list1[j]
            list1[j] = list1[i]
            list1[i] = var
        else:
            continue
print('sorted list in reverse order : ', list1)