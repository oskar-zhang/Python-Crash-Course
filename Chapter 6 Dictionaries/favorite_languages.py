favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + 
".")

#Looping Through All Key-Value Pairs
for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language is " + language.title())


#Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("\nHi " + name.title() + ", I see your favorite language is " + 
            favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

#Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#Looping Through All Values in a Dictionary
print("\nThe following languages have been mentioned: ")

for language in favorite_languages.values():
    print(language.title())

#Remove repeated values
for language in set(favorite_languages.values()):
    print(language.title())