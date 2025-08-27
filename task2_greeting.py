#ASSIGNMENT 1
#Module 2: Basic Python Concepts
"""
Task 2: Create a Personalized Greeting

Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.

"""

#1.  Takes a user's first name and last name as input.
first_name =input("Enter your first name:")
last_name =input("Enter ypur last name:")

#2.  Concatenates the first name and last name into a full name.
full_name= first_name+last_name

#3.  Prints a personalized greeting message using the full name.
print("Hello, ",full_name,"! Welcome to the Python program",sep="")
