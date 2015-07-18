# this imports 'features', which are better known as MODULES 
# they are pulled from Python 'feature sets', which are better known as LIBRARIES

# Here we are pulling the 'argv' module from the 'sys' library
# 'argv' is the "argument variable", a very common programming concept. The variable
# holds arguments you pass to it when you use the terminal to run the python script
from sys import argv

# This allows you to take the arguments that are passed to the script when you run it
# and assigns them to the variable(s) you associate to equal 'argv', the received arguments
# NOTE: that the amount of arguments passed to the script must match the amount of variables
# associated with 'argv'. Else, you will receive an error message. 
script, user_name, title = argv
prompt = 'Answer: '

# Prints text using %s string formatters and calling on the
# variables associated with argv to make a complete statement
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
# Not sure exactly, but uses the prompt variable above and places it before
# the text input when requested by the script. I believe this is called a PARAMETER
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
And you have a %r computer, working as a %r. Nice. 
I can tell that we are going to be friends.
""" % (likes, lives, computer, title)

print "Are you satisfied %s?" % user_name
satisfied = raw_input(prompt)

print "Excellent! Thank you for sharing your response of: \'%s\'" % satisfied