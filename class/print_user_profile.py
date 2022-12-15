"""
Imports: Using a program you wrote that has one function in it, store that function in a separate file . 
Import the function into your main program file, and call the function using each of these approaches:
"""
from import_user_profile import build_profile as bp

user_profile = bp('albert', 'einstein', 
                            location = 'princeton', 
                            field='physics')

print(user_profile)