def user_input():
    global a, b, c
    try:
        a = float(input("Enter length of one of the sides of the triangle 'a' : "))
        b = float(input("Enter length of one of the sides of the triangle 'b' : "))
        c = float(input("Enter length of one of the sides of the triangle 'c' : "))
    except ValueError:
        print("length cannot be interpreted as String")
        user_input()
    else:
        if find_the_type_of_triangle(a, b, c) == 'length cannot be zero or negative value':
            print(find_the_type_of_triangle(a, b, c))
            user_input()
        else:
            print(find_the_type_of_triangle(a, b, c))


def find_the_type_of_triangle(a: float, b: float, c: float):
    if not (a <= 0 or b <= 0 or c <= 0):
        if a == b == c:
            return 'it is an equilateral triangle'
        elif a == b and c != b or a == c and b != a or b == c and b != a:
            return 'it is an isosceles triangle'
        elif a != b != c:
            return 'it is a scalene triangle'
    else:
        return 'length cannot be zero or negative value'


user_input()