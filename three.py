"""
Make a list of the multiples of 3 from 3 to 30 . Use a for loop to print the numbers in your list 
"""

three = list(range(3, 30, 3))   # begin at three and sum three each time

for i in three:
    print(f"Multiples of three: {i}")