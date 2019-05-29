"""
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

sport = "Soccer"
print(sport == "Soccer")
print(sport == "Football")

print(sport.lower() == "Soccer")

answer = 12

if(answer <= 13 and answer >= 11):
    print(answer)
if(answer == 10 or answer == 12):
    print(answer)
else:
    print("Nothing")

num_list = [2, 4, 6, 8, 10]
speical_num =12
regular_num = 2

if speical_num not in num_list:
    print("Your special number is not special enough!")
if regular_num in num_list:
    print("Just a regular number.")