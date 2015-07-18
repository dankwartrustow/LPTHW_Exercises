# Imports argv module from sys library. 
from sys import argv
# Assigns two variables to argv. 
script, input_file = argv

# Creates function with 'f' variable. 
# Uses .read method on 'f' to read and print  entire file.
def print_all(f): 
    print f.read()

# This creates the function rewind, with another variable 'f'
# This takes the argument 'f' and seeks line 0, it appears.
def rewind(f):
    f.seek(0)

# Creates a module that takes two arguments for line count and f. 
# It prints the line being red, and uses the argument (line) to read it
def print_a_line(line_count, f):
    print line_count, f.readline()

# This creates a variable for the filename, using the variable above
# initially set as one of the argv arguments. 
current_file = open(input_file)


# This is essentially where the work starts to show. Everything up until this
# point has been housekeeping and preparation for what comes next.
 
# This line prints text and creates a new line for the print_all function. 
print "First let's print the whole file:\n"

# Calls function that prints out all text.
print_all(current_file)

# Prints text.
print "Now let's rewind, kind of like a tape."

# Calls the function to seek line '0', or the beginning of the file. 
rewind(current_file)

# Prints text.
print "Let's print three lines:"

# Sets a variable for the first line, 'current_line'.
# The function below takes in the two arguments using the current line
# and then the file name to allow the print_a_line function to work above
current_line = 1
print_a_line(current_line, current_file)

# Although seemingly redundant, you rename the 'current_line' variable in order 
# for the function above to work properly. By doing this you are able to 
# alter the core meaning of the variable over and over, and Python allows it. 

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
