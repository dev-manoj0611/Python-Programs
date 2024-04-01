rows = int(input('Please enter the total number of rows : '))
for i in range(1, rows + 1):
    if i == rows:
        print('* '*((rows*2)-1))
    else:
        print(' ' * (rows - i), end='')
        for j in range(1, i + 1):
            print('* ', end='')
        print(' ' * (((rows - i) * 2) - 2), end='')
        for k in range(1, i + 1):
            print('* ', end='')
        print()
