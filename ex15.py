# Lines 1-3 uses argv to get a filename. 
# Next we have line 5 where we use a new command open. 
# Right now, run pydoc open and read the instructions. 
# Notice how like your own scripts and raw_input, 
# it takes a parameter and returns a value you can set to your own variable. 
# You just opened a file.

#Line 7 prints a little message, but on line 8 we have something 
# very new and exciting. We call a function on txt named read. 
# What you get back from open is a file, and it also has commands 
# you can give it. You give a file a command by using the . 
# (dot or period), the name of the command, and parameters. 
# Just like with open and raw_input. The difference is that 
# txt.read() says, "Hey txt! Do your read command with no parameters!"



# from 'sys' library, pull the 'argv' module
from sys import argv
# assign 'script' and 'filename' variables to the argv module
script, filename = argv
# create variable 'txt' that opens the parameter provided by 'filename'
txt = open(filename)
# prints the name of the file
# second line performs the FUNCTION to read the file
print "Here's your file %r:" % filename
print txt.read()

# prompts you to type the filename in a second type
# uses '>' as a prompt to show the user where their text will appear
print "Type the filename again:"
file_again = raw_input ("> ")
# this provides a secondary method for opening the file
# it simply uses the open function
txt_again = open(file_again)
close_again = txt_again.close()
close_again

## print txt_again.read()