# This function is called add, which is passed 'a' and 'b'. It does two things
# first, it prints the string below using the two numbers
# second it returns the value of a + b to its original state, this will allow it to be run again
# if 'return' confuses you, run 'pydoc return' for additional context
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING % d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway. 
# Answer is -4391
# Start in the deepest set of parentheses and.. 
# first: identify the variables inside parenthesis 
# second: identify the method/function or variable that is to the left of each set of parenthesis
# this is what the identified variables are being passed to... 
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

