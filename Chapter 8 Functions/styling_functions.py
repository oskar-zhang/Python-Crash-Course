#Functions should have descriptive names, and these names should use
#lowercase letters and underscores.

"""
Every function should have a comment that explains concisely what
the function does. This comment should appear immediately after the
function definition and use the docstring format.
"""

#If you specify a default value for a parameter, no spaces should be used
#on either side of the equal sign:
"""
def function_name(parameter_0, parameter_1='default value'):
"""

#The same convention should be used for keyword arguments in function calls

"""
function_name(value_0, parameter_1='value')
"""


#If a set of parameters causes a function’s definition to
#be longer than 79 characters, press enter after the opening parenthesis on
#the definition line. On the next line, press tab twice to separate the list of
#arguments from the body of the function, which will only be indented one
#level.

"""
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
"""

#All import statements should be written at the beginning of a file.
#The only exception is if you use comments at the beginning of your file to
#describe the overall program.