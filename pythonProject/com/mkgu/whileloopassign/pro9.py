i = int(input('Specify the start of range : '))
j = int(input('Specify the end of range : '))
print('Odd numbers between the specified range are : ')
while i <= j:
    if i % 2 != 0:
        print(i)
    i += 1
