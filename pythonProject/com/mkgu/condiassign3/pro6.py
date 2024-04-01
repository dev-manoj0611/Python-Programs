def user_input():
    try:
        number = int(input("Please enter either a 3 digit or 4 digit number : "))
        if count_digits(number) is not None:
            print("Entered number has {} digits".format(count_digits(number)))
    except ValueError:
        print("String is not allowed / Enter Positive whole number only")
        user_input()


def count_digits(number: int):
    digit = 0
    while number != 0:
        number = int(number / 10)
        digit += 1
    if digit == 3 or digit == 4:
        return digit
    else:
        print("Enter either 3 or 4 digits only")
        user_input()


user_input()