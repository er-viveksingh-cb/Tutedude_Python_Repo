#ASSIGNMENT 2:
#Module 3: Control Structures in Python
"""
Task 2: Sum of Integers from 1 to 50 Using a Loop
 
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
 
"""
sum=0 #initalizing a the total sum as 0
for i in range(1,51): #interating the loop starting from 1 to 50
    sum +=i #adding i on each iteration
print("The sum of number from 1 to 50 is:",sum) #printng the total sum 
