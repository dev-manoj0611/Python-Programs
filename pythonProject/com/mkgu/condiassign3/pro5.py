def user_input():
    try:
        marks = int(input("Enter total marks : "))
        if 0 <= marks <= 100:
            print(generate_grade(marks))
        else:
            print('Input is out of Range / Enter in range 0 to 100')
            user_input()
    except ValueError:
        print('String is not allowed / Kindly Enter whole integer number')
        user_input()


def generate_grade(marks: int):
    if 100 >= marks > 90:
        return "your Grade is : A"
    elif 90 >= marks > 80:
        return "your Grade is : B"
    elif 60 <= marks <= 80:
        return "your Grade is : C"
    else:
        return "your Grade is : D"

user_input()