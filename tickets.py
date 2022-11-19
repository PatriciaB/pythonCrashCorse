"""
A movie theater charges different ticket prices depending on a person’s age . 
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; 
and if they are over age 12, the ticket is $15 . Write a loop in which you ask users their age, 
and then tell them the cost of their movie ticket 
"""

prompt = "What's you age? "

count = 0
while True:
    age = int(input(prompt))

    if age <= 3:
        print("Tre ticket is free.")
        break
    elif age <= 12:
        print("The ticket is $10.")
        break
    elif:
        print("The ticket is $25.")
        break

    

print(count)