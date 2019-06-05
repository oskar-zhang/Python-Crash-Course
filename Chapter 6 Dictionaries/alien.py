alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Accessing Values in a Dictionary
new_points = alien_0['points']

print("You just earned " + str(new_points) +" points!")


#Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

#Modifying Values in a Dictionary
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")