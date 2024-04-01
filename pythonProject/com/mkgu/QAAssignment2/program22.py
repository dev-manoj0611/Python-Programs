data= [(),('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
for i in data:
    if i==():
        data.remove(i)
print(data)
