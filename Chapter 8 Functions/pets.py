def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
#Multiple Function Calls
describe_pet('dog', 'willie')

#Keyword Arguments (Order doesn't matter)
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

#Default Values
def describe_pet1(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet1(pet_name='willie')
describe_pet1('willie')

#Because an explicit argument for animal_type is provided, Python will
#ignore the parameter’s default value.
describe_pet1(pet_name='harry', animal_type='hamster')