prompt = "> "
# create variable 'txt' that opens the parameter provided by 'filename'
print "Please enter your filename below."
filename = raw_input(prompt)
txt = open(filename)
# prints the name of the file
# second line performs the FUNCTION to read the file
print "Here's your file %r:" % filename
print txt.read()

close = txt.close()

close
