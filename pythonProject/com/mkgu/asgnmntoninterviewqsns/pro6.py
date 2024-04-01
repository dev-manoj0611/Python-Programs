list1 = []
print('Enter five integer elements : ')
for i in range(0, 5):
    inp = int(input())
    list1.append(inp)
for j in range(len(list1)):
    for k in range(j + 1, len(list1)):
        if list1[k] > list1[j]:
            var = list1[k]
            list1[k] = list1[j]
            list1[j] = var
print('sorted list in reverse order : ', list1)
