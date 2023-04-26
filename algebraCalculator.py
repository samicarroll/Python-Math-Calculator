__author__ = "Samantha Stilwell-Carroll"
"""Integration Project: Algebra 1 Calculator"""


"""Main Function"""


def main():
    continue_program = True
    while continue_program:
        print("Hello, please select one of the following Algebra 1 topic calculators.")
        print("1. Inequalities")
        print("2. Area of a triangle")
        print("3. Area of a square")
        print("4. Power of x calculator")
        print("5. Multiplication Calculator")
        print("6. Division Calculator")
        print("7. Practice Problems")
        print("8. Square Root Calculator")
        print("9. Find the Median")
        print("10. Absolute Value")
        print("11. Done.")
        user_choice = int(input())
        if user_choice == 1:
            print("Welcome to the inequality calculator.")
            print("This will decide if your question is true or false.")
            # a is a variable for the user to enter the first value
            # b is a variable for the user to enter the second value
            # c is a variable for which inequality is being chosen
            user_first_value = float(input("Enter the first value: "))
            user_second_value = float(input("Enter the second value: "))
            if user_first_value < user_second_value:
                print("The first value is less than the second value.")
            elif user_first_value > user_second_value:
                print("The first value is greater than the second value.")
            elif user_first_value >= user_second_value:
                print("The first value is less than or equal to the second value.")
            elif user_first_value <= user_second_value:
                print("The first value is greater than or equal to the second value.")
            elif user_first_value == user_second_value:
                print("The values are equal.")
            else:
                print("The values are not equal.")
        elif user_choice == 2:
            print("Welcome to the calculator for the area of a triangle.")
            print("This will calculate the triangles area from the numbers inputted.")
            # base is a variable for the "base" value of the triangle.
            # height is a variable for the height value of the triangle.
            # area is a variable for the area of a triangle
            base = float(input("Enter the base value of the triangle: "))
            height = float(input("Enter the height value of the triangle: "))
            area = base * height / 2
            print(area)
        elif user_choice == 3:
            side = int(input("Enter the length of the side: "))
            print(calculate_area(side))
        elif user_choice == 4:
            print("Welcome, this is a power calculator.")
            print("Enter the base value and exponent to find the value.")
            # a is a variable for the first value
            # b is a variable for the value of the exponent
            base_value = float(input("Enter the base value: "))
            exponent_value = float(input("Enter the exponent value: "))
            user_solution = base_value ** exponent_value
            print(user_solution)
        elif user_choice == 5:
            print("Welcome to the multiplication calculator.")
            value_one = float(input("Enter the first value: "))
            value_two = float(input("Enter the second value: "))
            user_solution = value_one * value_two
            print(user_solution)
        elif user_choice == 6:
            print("Welcome to the division calculator.")
            print("This calculator will solve any division problem!")
            a = float(input("Enter the value of the dividend: "))
            b = float(input("Enter the value of the divisor: "))
            quotient = a / b
            print(quotient)
        elif user_choice == 7:
            print("Welcome to the practice questions.")
            print("These are randomly generated to test your skills.")
            random_variable = 10
            random_variable += 20
            print("What would the value of x be if the equation was 10x?")
            print("30 = 10x")
            user_input = float(input("What is the x value: "))
            if user_input == 3:
                print("Good Job!")
            else:
                print("Try Again!")
        elif user_choice == 8:
            do_sqrt()
        elif user_choice == 9:
            print("Find the median.")
            print("This will print the numbers and median.")
            user_number = int(input("Enter a number: "))
            x = 1
            while x <= user_number:
                if x % 10 == 0:
                    print(x)  # Prints the x and new line
                else:
                    print(x, end=" ")  # Ends print statement with a space
                x = x + 1
            user_solution = (x - 1) / 2
            print("The median is:", user_solution)
        elif user_choice == 10:
            x = float(input("Enter a number: "))

            print("The absolute value of the number is:", abs(x))
        elif user_choice == 11:
            print("Thank you for trying my Algebra calculator!")
            print("Hope you enjoyed.")
            continue_program = False
        else:
            print("Invalid Selection, Try Again.")


"""Square Root Calculator"""


def do_sqrt():
    print("Square Root Calculator.")
    print("Determine if the number is a perfect square.")
    import math
    num = float(input("Enter a number: "))
    x = math.sqrt(num)
    if num % x == 0:
        print("Perfect Square")
    else:
        print("Not a Perfect Square")


def calculate_area(side):
    return side * side


"""Call To Main"""
main()
