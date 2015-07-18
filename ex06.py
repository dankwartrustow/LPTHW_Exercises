# %r is used for debugging since it displays the "raw" data of the variable
# %s and others are used for displaying to users

# variable with a decimal formatter inside the string
x = "There are %d types of people." % 10
# variable with a string
binary = "binary"
# variable with a string
do_not = "don't"
# variable of a string with two embedded formatters
y = "Those who know %s and those who %s." % (binary, do_not)

# both print variables
print x
print y

# prints string with formatters, but calling the poorly expressed variables above
# uses forced "r" method as the formatter
print "I said: %r." % x
# uses string formatter with additional apostraphes, 
# but which are still part of the string
print "I also said: '%s'." % y

# sets variables
# False in nonstring format, but can be printed
hilarious = False
# variable with string and forced formatter -whatever that means
joke_evaluation = "Isn't that joke so funny?! %r"

# prints variable while using 'hilarious' variable with
# the forced formatter from joke_evaluation, without formatter
# will create a variable undefined error "NameError"
print joke_evaluation % hilarious

# sets strings to two variables
w = "This is the left side of..."
e = "a string with a right side."

# concatenates both sets of variables and their stings
print w + e