p1=float(input("Enter the age of person 1 : "))
p2=float(input("Enter the age of person 2 : "))
p3=float(input("Enter the age of person 3 : "))
if p1>p2 and p1>p3:
    print("person 1 is the oldest")
elif p2>p1 and p2>p3:
    print("person 2 is the oldest")
else:
    print("person 3 is the oldest")
if p1<p2 and p1<p3:
    print("person 1 is the youngest")
elif p2<p1 and p2<p3:
    print("person 2 is the youngest")
else:
    print("person 3 is youngest")