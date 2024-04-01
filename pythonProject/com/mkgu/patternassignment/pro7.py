rows = int(input('Please enter the total number of rows : '))
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j < i:
            print('', end=' ')
        else:
            print('*', end=' ')
    print()
for k in range(2, rows+1):
    for l in range(rows, 0, -1):
        if l > k:
            print('', end=' ')
        else:
            print('*', end=' ')
    print()
