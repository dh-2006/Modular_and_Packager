
import datetime
import time
import math
import random
import string
import uuid

from utility_package import math_utilities
from utility_package import file_operations


# 1. Date and Time Menu
def date_menu():

    while True:
        print("\n--- DATE AND TIME ---")
        print("1. Current Date and Time")
        print("2. Difference Between Two Dates")
        print("3. Show Different Date Formats")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            today = datetime.datetime.now()
            print("Current Date and Time:", today)

        elif choice == "2":
            try:
                print("Enter First Date:")
                year1 = int(input("Year: "))
                month1 = int(input("Month: "))
                day1 = int(input("Day: "))

                print("Enter Second Date:")
                year2 = int(input("Year: "))
                month2 = int(input("Month: "))
                day2 = int(input("Day: "))

                date1 = datetime.date(year1, month1, day1)
                date2 = datetime.date(year2, month2, day2)

                difference = abs((date2 - date1).days)

                print("Difference:", difference, "days")

            except ValueError:
                print("Invalid date! Please enter a correct date.")

        elif choice == "3":
            today = datetime.date.today()

            print("Date:", today.strftime("%d-%m-%Y"))
            print("Date:", today.strftime("%d %B %Y"))
            print("Date:", today.strftime("%Y/%m/%d"))

        elif choice == "4":
            input("Press Enter to start.")
            start = time.time()

            input("Press Enter to stop.")
            end = time.time()

            print("Time Taken:", round(end - start, 2), "seconds")

        elif choice == "5":
            try:
                seconds = int(input("Enter seconds (1-3600): "))

                if seconds >= 1 and seconds <= 3600:
                    while seconds > 0:
                        print("Remaining:", seconds, "seconds")
                        time.sleep(1)
                        seconds = seconds - 1

                    print("Time is up!")

                else:
                    print("Enter seconds between 1 and 3600.")

            except ValueError:
                print("Please enter a whole number.")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


# 2. Mathematical Operations
def math_menu():

    while True:
        print("\n--- MATHEMATICAL OPERATIONS ---")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Area of Shapes")
        print("5. Logarithm")
        print("6. Kilometer to Miles")
        print("7. Celsius to Fahrenheit")
        print("8. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                number = int(input("Enter number (0-1000): "))

                if number >= 0 and number <= 1000:
                    answer = math_utilities.factorial(number)
                    print("Factorial:", answer)
                else:
                    print("Enter a number between 0 and 1000.")

            except ValueError:
                print("Please enter a whole number.")

        elif choice == "2":
            try:
                principal = float(input("Enter principal amount: "))
                rate = float(input("Enter interest rate (%): "))
                years = float(input("Enter time in years: "))

                if principal < 0 or rate < 0 or years < 0:
                    print("Values cannot be negative.")
                else:
                    amount = principal * (1 + rate / 100) ** years
                    print("Final Amount:", round(amount, 2))
                    print("Compound Interest:",
                          round(amount - principal, 2))

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "3":
            try:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                print("Sine:", round(math.sin(radians), 4))
                print("Cosine:", round(math.cos(radians), 4))

                if abs(math.cos(radians)) < 0.0000001:
                    print("Tangent is undefined for this angle.")
                else:
                    print("Tangent:", round(math.tan(radians), 4))

            except ValueError:
                print("Please enter a valid angle.")

        elif choice == "4":
            print("1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape = input("Choose shape: ")

            try:
                if shape == "1":
                    radius = float(input("Enter radius: "))

                    if radius >= 0:
                        area = math.pi * radius * radius
                        print("Circle Area:", round(area, 2))
                    else:
                        print("Radius cannot be negative.")

                elif shape == "2":
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))

                    if length >= 0 and width >= 0:
                        print("Rectangle Area:", length * width)
                    else:
                        print("Dimensions cannot be negative.")

                elif shape == "3":
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))

                    if base >= 0 and height >= 0:
                        print("Triangle Area:", 0.5 * base * height)
                    else:
                        print("Dimensions cannot be negative.")

                else:
                    print("Invalid shape choice.")

            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "5":
            try:
                number = float(input("Enter a positive number: "))

                if number > 0:
                    print("Natural Log:", round(math.log(number), 4))
                    print("Base-10 Log:", round(math.log10(number), 4))
                else:
                    print("Number must be greater than zero.")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "6":
            try:
                km = float(input("Enter distance in kilometers: "))
                if km >= 0:
                    print("Distance in Miles:", round(km * 0.621371, 3))
                else:
                    print("Distance cannot be negative.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "7":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print("Temperature in Fahrenheit:", round(fahrenheit, 2))
            except ValueError:
                print("Please enter a valid temperature.")

        elif choice == "8":
            break

        else:
            print("Invalid choice!")


# 3. Random Data Generation
def random_menu():

    while True:
        print("\n--- RANDOM DATA GENERATION ---")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Random Sampling")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                low = int(input("Enter minimum number: "))
                high = int(input("Enter maximum number: "))

                if low <= high:
                    print("Random Number:", random.randint(low, high))
                else:
                    print("Minimum cannot be greater than maximum.")

            except ValueError:
                print("Enter whole numbers only.")

        elif choice == "2":
            try:
                low = int(input("Enter minimum number: "))
                high = int(input("Enter maximum number: "))
                count = int(input("How many numbers (1-100): "))

                if low > high:
                    print("Minimum cannot be greater than maximum.")
                elif count < 1 or count > 100:
                    print("Enter list size between 1 and 100.")
                else:
                    numbers = []

                    for i in range(count):
                        numbers.append(random.randint(low, high))

                    print("Random List:", numbers)

            except ValueError:
                print("Enter whole numbers only.")

        elif choice == "3":
            try:
                length = int(input("Password length (8-64): "))

                if length >= 8 and length <= 64:
                    characters = string.ascii_letters + string.digits + "!@#$%"
                    password = ""

                    for i in range(length):
                        password = password + random.choice(characters)

                    print("Generated Password:", password)

                else:
                    print("Password length must be 8 to 64.")

            except ValueError:
                print("Enter a whole number.")

        elif choice == "4":
            try:
                length = int(input("OTP length (4-8): "))

                if length >= 4 and length <= 8:
                    otp = ""

                    for i in range(length):
                        otp = otp + str(random.randint(0, 9))

                    print("OTP:", otp)
                    

                else:
                    print("OTP length must be 4 to 8.")

            except ValueError:
                print("Enter a whole number.")

        elif choice == "5":
            data = input("Enter items separated by commas: ")
            items = []

            for item in data.split(","):
                item = item.strip()

                if item != "":
                    items.append(item)

            if len(items) == 0:
                print("Please enter some items.")
            else:
                try:
                    count = int(input("How many items to select? "))

                    if count >= 1 and count <= len(items):
                        print("Random Sample:",
                              random.sample(items, count))
                    else:
                        print("Enter a valid sample size.")

                except ValueError:
                    print("Enter a whole number.")

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


# 4. Generate UUID
def generate_uuid():
    print("Your Unique ID:", uuid.uuid4())


# 5. Explore Modules
def explore_modules():

    print("\n--- EXPLORE MODULES ---")
    print("1. Math")
    print("2. Random")
    print("3. DateTime")
    print("4. UUID")
    print("5. Time")
    print("6. Custom Math Utilities")
    print("7. File Operations Module")

    choice = input("Choose module: ")

    if choice == "1":
        print(dir(math))
    elif choice == "2":
        print(dir(random))
    elif choice == "3":
        print(dir(datetime))
    elif choice == "4":
        print(dir(uuid))
    elif choice == "5":
        print(dir(time))
    else:
        print("Invalid choice!")


# Main Menu
while True:
    print("\n===== MULTI-UTILITY TOOLKIT =====")
    print("1. Date and Time")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Explore Modules")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date_menu()

    elif choice == "2":
        math_menu()

    elif choice == "3":
        random_menu()

    elif choice == "4":
        generate_uuid()

    elif choice == "5":
        file_operations.file_menu()

    elif choice == "6":
        explore_modules()

    elif choice == "7":
        print("Thank you! Program closed.")
        break

    else:
        print("Invalid choice! Enter 1 to 7.")
