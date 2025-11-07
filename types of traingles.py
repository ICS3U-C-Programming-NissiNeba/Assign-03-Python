#!/usr/bin/env python3
# Created By: Your Name Nissi
# Date: Month Day, Year october 2025
# This program generates a random number between 0 and 9
# and asks the user to guess the number. It then tells the user if the number is positive ,negative or zero
#!/usr/bin/env python3
# Created By: Your Name Nissi
# Date: October 2025
# This program asks the user for the sides of a traingle and the computer tells 
# him if the traingle is isoceles scalene or equitaleral

def main():
    try:
        # Ask the user for the three sides
        side1 = int(input("Enter the first side: "))
        side2 = int(input("Enter the second side: "))
        side3 = int(input("Enter the third side: "))

        # Check if sides are positive
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            print("A side cannot be zero or negative.")
        
        # Classify the triangle
        if side1 == side2 == side3:
            print("This is an equilateral triangle.")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("This is an isosceles triangle.")
        else:
            print("This is a scalene triangle.")

    except ValueError:
        print("please enter a valid integer.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
