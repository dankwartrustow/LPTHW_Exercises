# this one is like your scripts with argv
# the (*args) is very similar to argv, except that this format is
# specifically used with functions. Not sure why importing not needed

# this exercise is used to teach you FUNCTIONS, aka 'mini-scripts'
# the * tells Python to take all the arguments to the function and 
# then put them in 'args' as a list. It's like 'argv' that you've
# been using, but for functions. It's not normally used too often unless
# specifically needed. 
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes on argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."


print_two("Jon","Hernandez")
print_two_again("Jon","Hernandez")
print_one("First!")
print_none()
