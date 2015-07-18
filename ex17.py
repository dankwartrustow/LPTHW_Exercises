# imports argv module from sys library
from sys import argv
# imports exists module from os.path library
from os.path import exists

# assigns variables to argv, to be entered upon running the script
script, from_file, to_file = argv
# prints text and calls two string formatters to present to the end user
print "Copying from %s to %s"  % (from_file, to_file)

# we could do these two on one line, how?
# NO FUCKING CLUE how to make this whole thing one line
# in_file opens the file passed to the script using the argv
# variable 'from_file'. It then calls the read method on 
# in_file, and assigns it to the variable 'indata'
# it is unclear whether read() is providing bytes or word count
in_file = open(from_file) ; indata = in_file.read()

# appears like it's calling a decimal(number) formatter, and rather
# than calling a variable, you can run a method on the spot
print "The input file is %d bytes long" % len(indata)

# similar to the len method used above, Zed shows a different way
# that formatters may be leveraged. However, creating variables
# may be more organized overall
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("?")

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
