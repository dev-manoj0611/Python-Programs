list1 = [100, 56, 9, 55, 19, 11, 3, 50]
min = list1[0]
for i in range(0, len(list1)):
    if list1[i] < min:
        min = list1[i]
print(min)