"""
Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
• Print the message, The first three items in the list are: . Then use a slice to print the first three items from that 
program’s list .
• Print the message, Three items from the middle of the list are: . Use a slice to print three items from the 
middle of the list .
• Print the message, The last three items in the list are: . Use a slice to print the last three items in the list 
"""
players = ['P1', 'P2', 'P3', 'P4', 'P5']

#First three items
print("The first three items in the list are: ")
for player in players[:3]:
    print(player.title())

print("Three items from the middle of the list are:")
for player in players[1:4]:
    print(player.title())

print("The last three items in the list are:")
for player in players[2:]:
    print(player.title())

