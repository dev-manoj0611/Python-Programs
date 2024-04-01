print("Price of a water bottle : Rs. 20")
print("10% discount on orders above \"Rs. 1000\"")
def biller(qty):
    if 20*qty>=1000:
        print("************** BILL GENERATED ***************")
        print("bill amount : Rs.",20*qty)
        print("discount applied : 10% (Rs.",(20*qty)*0.1,")")
        print("total payable : Rs.",(20*qty)-(20*qty)*0.1)
        print("**************** THANK YOU ******************")
    elif 20*qty>=20 and 20*qty<1000:
        print("************** BILL GENERATED ***************")
        print("bill amount : Rs.",20*qty)
        print("discount applied : 0% (Rs. 0.00)")
        print("total payable : Rs.",20*qty)
        print("**************** THANK YOU ******************")
    else:
        print("PLEASE ENTER POSITIVE INTEGER")
        receiver()
def receiver():
    data=True
    while(data==True):
        try:
            qty=int(input("Enter the quantity of water bottle to be billed : "))
            data=False
        except ValueError:
            print("QUANTITY CANNOT BE ANYTHING EXCEPT POSITIVE INTEGER")
        else:
            biller(qty)
receiver()