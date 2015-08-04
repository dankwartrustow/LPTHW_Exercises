# 3 Rules for using While-Loops
# 1. Make sure that you use while-lopos sparingly. Usually a for-loop is better. 
# 2. Review your while statements and make sure that the thing you are testing will become
# False at somepoint. 
# 3. When in doubt, print out your test variable at the top and bottom of the while-loop 
# to see what it's doing.

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers: 
	print num

