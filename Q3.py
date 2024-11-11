#Q3. Write a function to compute the least common multiple (LCM) of two numbers using the Greatest Common Divisor (GCD) method.

import math
def lcm(a,b):
    return abs(a*b)
    

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print(f"The LCM of {a} and {b} is: {lcm(a, b)}")
except ValueError:
    print("Please enter valid integers.")