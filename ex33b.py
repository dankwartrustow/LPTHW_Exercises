i = 0
numbers = []
numero = 10

def function_while(n):
	
	while n < 100:
		print "At the top n is %d" % n
		numbers.append(n)

		n += numero
		print "Numbers now: ", 

		print "Numbers now: ", numbers
		print "At the bottom n is %d" % n

	print "The numbers: "

	for num in numbers:
		print num


print "Put in a number under 100!"

running = function_while(44)

running