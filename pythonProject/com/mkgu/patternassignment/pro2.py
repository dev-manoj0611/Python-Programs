rows = int(input('Please enter the total number of rows : '))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j < i:
            print(' ', end=' ')
        else:
            print('*', end=' ')
    print()
