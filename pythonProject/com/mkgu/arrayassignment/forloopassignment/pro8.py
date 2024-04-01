m = int(input('Please specify the begin of range : '))
n = int(input('Please specify the end of range : '))
for i in range(m, n + 1):
    if i % 2 == 0:
        print(i, 'is even')
    else:
        print(i, 'is odd')