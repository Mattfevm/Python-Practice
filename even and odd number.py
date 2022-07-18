""" 
Challenge 
Determine if a number is even or odd number

Create a script  that if the number entered is  Odd print true otherwise false.
"""

num=int(input("Please enter a integer number: "))
if (num % 2 ) == 0:
    print(f"{num} is Even number")
else:
    print(f"{num} is Odd number")