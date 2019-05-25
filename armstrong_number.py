"""
This program is all about Armstrong Numbers.
An Armstrong number  three digits is an integer 
such that the sum of the cubes of its digits is equal to the number itself.
For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.
"""

num1=int(input("Enter the number"))    #Takes value from user in form of integer 

sum=0  # defined sum(variable) as zero

# find the sum of the cube of each digit

temp = num1
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# displaying the final output
if num1 == sum:
    print(num1, "is an Armstrong number")
    
else:
    print(num1, "is not an Armstrong number")
    
