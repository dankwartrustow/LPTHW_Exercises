from sys import exit
# -*- coding: utf-8 -*-


print "Welcome to If, by Rudyard Kipling. This script will help you memorize this amazing poem."
print "Press Enter to begin! Remember to use Ctrl + C to escape at any time."
raw_input("")
name = raw_input("Please enter your name. \n> ")
print "It's nice to see you %s, thanks for playing." % name
print "Your progress will be saved in Your_Score.txt"

begin = raw_input("Ready? \nyes/no:")

if begin == "no":
    print "Until next time, then %s!" % name
    exit(0)
elif begin == "yes":
    print ""
    
# 'one' refers to phrase one, naming of methods will follow this. 
def v1i():
    print "1. " + "If you can keep your head when all about you\n    Are losing theirs and blaming it on you,"
    print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
    print "3. " + "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch,"
    print "4. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
    one_choice = raw_input("What's the first phrase?\n1,2,3,4? ")
    if one_choice == "1":
    	print "Correct!\n"
    elif one_choice == "2" or "3" or "4":
    	print "Sorry, try again!"
    	v1i()
v1i()

def v1ii():
	print "If you can keep your head when all about you\n    Are losing theirs and blaming it on you,..."
	print "1. " + "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,"
	print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
	print "3. " + "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;"
	print "4. " + "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;"
	two_choice = raw_input("What's the second phrase?\n1,2,3,4? ")
	if two_choice == "3":
		print "Correct!\n"
	elif two_choice == "1" or "2" or "4":
		print "Sorry, try again!"
v1ii()

def v1iii():
	print "1. " + ""
	print "2. " + ""
	print "3. " + ""
	print "4. " + ""

def v1iv():
	print "1. " + ""
	print "2. " + ""
	print "3. " + ""
	print "4. " + ""