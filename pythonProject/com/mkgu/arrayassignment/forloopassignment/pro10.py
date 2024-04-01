j = 50
first = 0
second = 1
for i in range(0, j):
    value = first + second
    if value > j:
        break
    print(value)
    first = second
    second = value