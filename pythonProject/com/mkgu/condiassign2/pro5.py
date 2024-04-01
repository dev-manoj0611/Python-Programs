inp=int(input("Enter positive integer : "))
unit=inp%10
if unit%3==0:
    print("the last/unit place digit",unit,"is divisible by 3")
else:
    print("the last/unit place digit",unit,"is not divisible by 3")