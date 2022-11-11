"""
Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually 
starts at one and ends at one million . Also, use the sum() function to see how quickly Python can add a million numbers 
"""

list = []
for i in range(1000000):
    list.append(i+1)

print(f"Min: {min(list)}")
print(f"Max: {max(list)}")

print(f"Sum: {sum(list)}")