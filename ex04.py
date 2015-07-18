cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
#provides a variable for total empty vehicles
cars_not_driven = cars - drivers
#equals the amount of drivers to not calculate drivers by space in car
cars_driven = drivers
#this is accurate by saying "we can transport x amount of people today"
#however this would not be an accurate way of calculating the number of non-driving
#passengers that could fit in each vehicle, wonder if theres another way of calculating
carpool_capacity = cars_driven * space_in_a_car
#space in car doesn't appear to be used at all in this
#this divides passengers by cars driven for a circa number of people who can fit in each
#I wonder if there's a more exact way to do this... 
average_passengers_per_car = passengers / cars_driven

#prints total number of cars
print "There are", cars, "cars available."
#prints total amount of available drivers
print "There are only", drivers, "drivers available."
#shows the total amount of empty cars which won't be driven
print "There will be", cars_not_driven, "empty cars today."
#shows total number of drivers and passengers able to be driven, total
print "We can transport", carpool_capacity, "people today."
#shows total number of available passengers
print "We have", passengers, "to carpool today."
#shows average passengers per vehicle
print "We need to put about", average_passengers_per_car, "in each car."