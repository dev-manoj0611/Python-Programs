rows = int(input('Please enter the total number of rows : '))
for i in range(1, int((rows / 2) + 2)):
    if i < int((rows / 2) + 1):
        print('* ' * i, end='' + ' ' * ((rows * 2) - (i * 4)) + '* ' * i)
    elif i == int((rows / 2) + 1):
        print('* ' * rows, end='')
    print()
for j in range(int(rows / 2), 0, -1):
    for k in range(2, ((rows * 2) + 1), 4):
        print('* ' * j + (' ' * k) )
    print()
