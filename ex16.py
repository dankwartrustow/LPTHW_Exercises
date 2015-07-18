# from 'sys' library, import 'argv' module
from sys import argv
# sets two variables for argv
script, filename = argv
# prints text and calls raw formatter of the filename input when the file is run
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# this is the "prompt" for the user input, in this case they're asked RETURN
raw_input("?")

print "Opening the file..."
# creates a variable called target, but does not actually do anything with it yet
target = open(filename, 'w')
# this calls target, which opens the file with 'w' which is likely write persmissions
# it then truncates (empties) the file. 
# target = variable, truncate = method, () = parameter
print "Truncating the file. Goodbye!"
# prints text
print "Now I'm going to ask you for three lines."
# simply takes in text with a preceeding prompt and adds it to variables
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
# calls target variable which opens file with write permission, then uses write method;
# write method alternates between writing a variable and then a string. 
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.close()

txt = open(filename)
print "Here's what you wrote:"
print txt.read()
print "When you're finished, hit RETURN"
raw_input (">")
print "And finally, we close it."
txt.close