the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# It's important to note that 'number' is a variable being defined by the
# for-loop. It initializes the variable to the current element of the loop 
# iteration, each time through.
# Structure: for instance/permanent variable in list variable, do x 
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits: 
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one 
elements = []

# then use the range function to do 0 to 5 counts
#for i in range(6)
#	print "Adding %d to the list." % i
	#append is a function that lists understand
#	elements.append(i)

# Study Drill #2: Could you have avoided that for-loop entirely on line 22 and 
# just assigned range(0,6) directly to elements?
elements.append(range(0, 6))

# now we can print them out too
for i in elements: 
	print "Element was: %r" % i
### Getting error here "TypeError: %d format: a number is required, not list"

two_dimensional = [[1,2,3,4],['a','b','c','d',]]

print two_dimensional