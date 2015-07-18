# This exercise in general appears to give context to using raw_input
# raw_input will take "genera" non-contextual input from the user
# it lacks some of the features that "input" has, but as a rule of thumb
# raw_input is much more secure, as it doesn't automatically run "input" 
# items as code

# Prints text asking questions, and assigns a user's raw input to values
print "How old are you?", 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# prints text, uses raw formatters, and calls on multiple variables
print "So, you're %r old, %r tall, and %r heavy." % (
	age, height, weight)


print "What's your favorite book?"
fav_book = raw_input()
print "How many pages are in the book?"
pages = int(raw_input())
print "How big is your dick?"
dick = int(raw_input())

muhhfucka = pages - dick

print "My favorite book is %r, muhhfucka." % fav_book
print "%r is %r bigger than your dick!" % (fav_book, muhhfucka)