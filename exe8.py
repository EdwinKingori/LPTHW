#Using a function to turn the formatter variabe into strings.

formatter  = "{} {} {} {}"

"""
formatter.format(...) does the following : 
Takes the format string defined in line 3.
Calls its format function
Tells python to pass to format four arguments, which match up with the four {placeholders} in the formatter variable.
The result of calling format on formatter is a new string that has the {} replaced with the four variables.
"""

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))

print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format( 
      "Try your",
      "Own text here", 
      "Maybe a poem", 
      "or a song about fear"
))      
