#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Get the last digit considering the sign of the original number
last_digit = number % 10

string = "Last digit of"

print("{} {} is {} and is".format(string, number, last_digit), end=" ")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
