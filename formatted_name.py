# A function that takes a first and last name, and returns a neatly formatted full name
#To make get_formatted_name() work without a middle name, we set the default value of middle_name to 
# an empty string and move it to the end of the list of parameters

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)