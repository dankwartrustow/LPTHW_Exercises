name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
centimeter_multiplier = 2.54 # centimeters = 1 inch
pound_multiplier = .453592 # kilograms = 1 pound
metric_height = height * centimeter_multiplier # transforms inches to centimeters
metric_weight = weight * pound_multiplier # transforms pounds to kilograms

# %s calls a string
# %d calls a decimal
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "In England he is %d centimeters tall" % metric_height
print "He's %d pounds heavy." % weight
print "In England he is %d kilograms heavy" %metric_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight )