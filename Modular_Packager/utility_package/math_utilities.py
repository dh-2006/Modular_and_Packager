import math



def factorial(number):
    answer = 1

    for i in range(1, number + 1):
        answer = answer * i

    return answer



def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount



def circle_area(radius):
    return math.pi * radius * radius



def rectangle_area(length, width):
    return length * width


def triangle_area(base, height):
    return 0.5 * base * height



def km_to_miles(km):
    return km * 0.621371



def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
