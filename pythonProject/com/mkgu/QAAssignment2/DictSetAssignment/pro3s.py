s={1,2,3,4,5}
print(s)
inp=int(input("Enter a number to remove from set s : "))
s1={inp}
if s1.issubset(s):
    s.remove(inp)
    print(s)
else:
    print("element",inp,"not found")