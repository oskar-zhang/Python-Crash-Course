"""
8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

def build_profile (firstname, lastname, **description):
    myself = {}
    myself['First Name'] = firstname
    myself['Last Name'] = lastname

    for key, value in description.items():
        myself[key.title()] = value.title()
    
    return myself

my_profile = build_profile('Oskar', 'Zhang', Glass = 'Yes', Race = 'Asian', 
                            sports = 'soccer')

print(my_profile)























"""
def build_profile(first, last, **characteristics):
    profile = {}
    profile['First Name'] = first.title()
    profile['Last Name'] = last.title()
    for key, value in characteristics.items():
        profile[key] = value.title()
    return profile

myself = build_profile('oskar', 'zhang', Race = 'asian', 
                Job = 'developer', Nationality = 'china')

print(myself)
"""