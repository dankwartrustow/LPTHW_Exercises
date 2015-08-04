people = 40
cars = 20
buses = 15

# 'elif' is the next possible outcome after if. This will
# only occur if 'if' is not met. 'else' is what this block
# of code resolves to if none of the previous parameters
# are met. 
if cars > people: 
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses and cars < people:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."