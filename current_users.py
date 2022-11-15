"""
Do the following to create a program that simulates how websites ensure that everyone has a unique username .
• Make a list of five or more usernames called current_users . • Make another list of five usernames called new_users . 
Make sure one or two of the new usernames are also in the current_users list .
• Loop through the new_users list to see if each new username has already been used . 
If it has, print a message that the person will need to enter a new username . 
If a username has not been used, print a message saying that the username is available .
• Make sure your comparison is case insensitive . If 'John' has been used, 'JOHN' should not be accepted 
"""

users = ['Harry', 'Ron', 'Hermione', 'Hagrid', 'Draco']
for i in range(len(users)):
    users[i] = users[i].lower()

new_users = ['Luna', 'Ginny', 'Ron', 'Harry', 'George']
for i in range(len(new_users)):
    new_users[i] = new_users[i].lower()


for user in new_users:
    if user in users:
        print("You need to enter a new username")
    else:
        print(f"The username {user.title()} is avaliable")