inp = input('Enter a number : ')
st = str(inp)
count=0
if inp.isdigit():
    for i in range(len(st)):
        if int(inp)!=0:
            inp=int(inp)/10
            count+=1
    print(count)
else:
    print('Please enter int literals')