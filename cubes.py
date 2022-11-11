"""
A number raised to the third power is called a cube . For example, the cube of 2 is written as 2**3 in Python . 
Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to 
print out the value of each cube 
"""

number = list(range(10))
cubes =[]

for i in number:
    cube = (i+1)**3
    cubes.append(cube)
    print(f"Cube de {i+1}: {cube}")