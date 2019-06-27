"""
def get_formatted_name(first_name, last_name):
    #Return a full name, neatly formatted.
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
"""

#Making an Argument Optional

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

#If we’re using a middle name, however, we have to make sure the middle
#name is the last argument passed so Python will match up the positional
#arguments correctly

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

