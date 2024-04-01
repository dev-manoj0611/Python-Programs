def user_input():
    try:
        units = int(input("Enter total units : "))
        if not units < 0:
            print(generate_bill(units))
        else:
            print('Negative integer is not allowed')
            user_input()
    except ValueError:
        print('String is not allowed / Kindly Enter whole integer number')
        user_input()


def generate_bill(units: int):
    rate_1, rate_2 = 5, 10
    if 100 >= units >= 0:
        return "your bill is : 0.00 Rs"
    elif 200 >= units > 100:
        charges = units - 100
        return "your bill is : {} Rs".format(charges * rate_1)
    elif units > 200:
        charges_1 = 100 * rate_1
        charges_2 = (units - 200) * rate_2
        return "your bill is : {} Rs".format(charges_1+charges_2)


user_input()