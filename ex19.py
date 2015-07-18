# This section defines the function. The variables set within the 
# function are not callable outside of the function (in the script). 
# You can then pass arguments in the form of strings, decimals, or 
# variables to the function. These arguments then take on the form of
# the function's variables, and perform the needed action. 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# This section passes decimals to the function directly. 
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# This section creates variables of decimals, which are passed to
# the function without issue. 
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This section pases calculated decimals as args to the function.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# This section passes calculated decimals, calculated from variables.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
