aliens_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x_position: {str(aliens_0['x_position'])}")


#Move the alien to the right
#Determine how fat to move the alien based on tis current speed.
if aliens_0['speed'] == 'slow':
    x_increment = 1
elif aliens_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien.
    x_increment = 3

#The new positions is the old position plis the increment
aliens_0['x_position'] = aliens_0['x_position'] + x_increment

print(f"New x_position: {str(aliens_0['x_position'])}")
