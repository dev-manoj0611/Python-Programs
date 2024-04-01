print('Numbers between 1 and 100 that are divisible by 9 are : ')
i = 1
while i in range(1, 101):
    if i % 9 == 0:
        print(i, 'is divisible by 9')
    i += 1
