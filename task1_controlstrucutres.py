#ASSIGNMENT 2
# Module 3: Control Structures in Python
"""
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

"""
num = int(input("Enter a number:")) #take a number as input from user
if (num%2==0): #logic used:a number is even when it gives 0 as reminder when devided by 2
    print(num,"is a even number.") #prints the statment when test epression of if statement is true 
else:
    print(num,"is a odd number") #else this statement will be printed 

