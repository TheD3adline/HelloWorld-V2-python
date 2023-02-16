"""
    Author: Michael Fessler
    Date: 2023/02/16
    Version: 0.1
    Description:
            First script of my personal python relaunch.
"""

userName = input("Please enter your name: ")

print("Welcome " + userName + ", now please enter 3 numbers: ")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")
sumNums = float(num1) + float(num2) + float(num3)
avgNums = (float(num1) + float(num2) + float(num3)) / 3

print("The sum of your numbers is: " + str(sumNums))
print("The average of your numbers is: " + str(avgNums))