# -*- coding: utf-8 -*-
import sys
import datetime
from sys import exit

print "\nWelcome to If, by Rudyard Kipling. This script will help you memorize this amazing poem."
print "Press Enter to begin! Remember to use Ctrl + C to escape at any time."
raw_input("")
name = raw_input("Please enter your name. \n> ")
print "It's nice to see you %s, thanks for playing." % name
print "Your progress will be saved in ex36Your_Score.txt"

beginv1 = raw_input("Ready? \nyes/no:")
if beginv1 == "no":
    print "Until next time, %s!" % name
    exit(0)
elif beginv1 == "yes":
    print ""
    
#### VERSE ONE ####

def v1i():
    print "1. " + "If you can keep your head when all about you\n    Are losing theirs and blaming it on you," #
    print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
    print "3. " + "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch,"
    print "4. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
    v1i_choice = raw_input("What's the first phrase?\n1,2,3,4? ")
    if v1i_choice == "1":
    	print "Correct!\n"
    elif v1i_choice == "2" or "3" or "4":
    	print "Sorry, try again!"
    	v1i()
v1i()

def v1ii():
	print "If you can keep your head when all about you\n    Are losing theirs and blaming it on you,..."
	print "1. " + "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,"
	print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
	print "3. " + "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;" #
	print "4. " + "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;"
	v1ii_choice = raw_input("What's the second phrase?\n1,2,3,4? ")
	if v1ii_choice == "3":
		print "Correct!\n"
	elif v1ii_choice == "1" or "2" or "4":
		print "Sorry, try again!"
		v1ii()
v1ii()

def v1iii():
	print "If you can keep your head when all about you\n    Are losing theirs and blaming it on you,"
	print "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;..."
	print "1. " + "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,"
	print "2. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies," #
	print "3. " + "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;"
	print "4. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
	v1iii_choice = raw_input("What's the third phrase?\n1,2,3,4? ")
	if v1iii_choice == "2":
		print "Correct!\n"
	elif v1iii_choice == "1" or "3" or "4":
		print "Sorry, try again!"
		v1iii()
v1iii()

def v1iv():
	print "If you can keep your head when all about you\n    Are losing theirs and blaming it on you,"
	print "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;"
	print "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,..."
	print "1. " + "Or being hated, don’t give way to hating,\n    And yet don’t look too good, nor talk too wise:" #
	print "2. " + "Or watch the things you gave your life to, broken,\n    And stoop and build ’em up with worn-out tools:"
	print "3. " + "And lose, and start again at your beginnings\n    And never breathe a word about your loss;"
	print "4. " + "And so hold on when there is nothing in you\n    Except the Will which says to them: ‘Hold on!’" 
	v1iv_choice = raw_input("What's the fourth phrase?\n1,2,3,4? ")
	if v1iv_choice == "1":
		print "Correct!\n"
	elif v1iv_choice == "2" or "3" or "4":
		print "Sorry, try again!"
		v1iv()
v1iv()

def v1cont():
	print "You've completed the first verse! There are three left. Would you like to review it before continuing, just continue, or quit and save your progress?"
	beginv2 = raw_input("review/continue/quit:")
	if beginv2 == "quit":
		print "Until next time, %s! Don't forget to follow your progress in ex36Your_Score.txt" % name
		with open("ex36Your_Score.txt", mode='a') as file:
			file.write("%s 25%% complete at %s" % (name, datetime.datetime.now()))
		exit(0)
	elif beginv2 == "continue":
		print ""
	elif beginv2 == "review":	
		print "VERSE ONE\nIf you can keep your head when all about you\n    Are losing theirs and blaming it on you,"
		print "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;"
		print "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
		print "Or being hated, don’t give way to hating,\n    And yet don’t look too good, nor talk too wise:"
v1cont()

#### VERSE TWO ####

def v2i():
    print "\nVERSE TWO" 
    print "1. " + "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;"
    print "2. " + "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch," 
    print "3. " + "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;" #
    print "4. " + "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;" 
    v2i_choice = raw_input("What's the first phrase?\n1,2,3,4? ")
    if v2i_choice == "3":
    	print "Correct!\n"
    elif v2i_choice == "1" or "2" or "4":
    	print "Sorry, try again!"
    	v2i()
v2i()

def v2ii():
    print "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;..."
    print "1. " + "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch,"
    print "2. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
    print "3. " + "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone,"
    print "4. " + "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;" # 
    v2ii_choice = raw_input("What's the second phrase?\n1,2,3,4? ")
    if v2ii_choice == "4":
    	print "Correct!\n"
    elif v2ii_choice == "1" or "2" or "3":
    	print "Sorry, try again!"
    	v2ii()
v2ii()

def v2iii():
    print "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;"
    print "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;..."
    print "1. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools," #
    print "2. " + "And lose, and start again at your beginnings\n    And never breathe a word about your loss;"
    print "3. " + "If you can fill the unforgiving minute\n    With sixty seconds’ worth of distance run,"
    print "4. " + "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;"
    v2iii_choice = raw_input("What's the third phrase?\n1,2,3,4? ")
    if v2iii_choice == "1":
    	print "Correct!\n"
    elif v2iii_choice == "2" or "3" or "4":
    	print "Sorry, try again!"
    	v2iii()
v2iii()

def v2iv():
    print "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;"
    print "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;"
    print "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,..."
    print "1. " + "And lose, and start again at your beginnings\n    And never breathe a word about your loss;"
    print "2. " + "Or being hated, don’t give way to hating,\n    And yet don’t look too good, nor talk too wise:"
    print "3. " + "And so hold on when there is nothing in you\n    Except the Will which says to them: ‘Hold on!’"
    print "4. " + "Or watch the things you gave your life to, broken,\n    And stoop and build ’em up with worn-out tools:" #
    v2iv_choice = raw_input("What's the fourth phrase?\n1,2,3,4? ")
    if v2iv_choice == "4":
    	print "Correct!\n"
    elif v2iv_choice == "1" or "2" or "3":
    	print "Sorry, try again!"
    	v2iv()
v2iv()

def v2cont():
	print "You've completed the second verse! There are two left. Would you like to review your progress before continuing, just continue, or quit and save your progress?"
	beginv2 = raw_input("review/continue/quit:")
	if beginv2 == "quit":
		print "Until next time, %s! Don't forget to follow your progress in ex36Your_Score.txt" % name
		with open("ex36Your_Score.txt", mode='a') as file:
			file.write("\n%s 50%% complete at %s" % (name, datetime.datetime.now()))
		exit(0)
	elif beginv2 == "continue":
		print ""
	elif beginv2 == "review":	
		print "VERSE ONE"
		print "If you can keep your head when all about you\n    Are losing theirs and blaming it on you,"
		print "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;"
		print "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
		print "Or being hated, don’t give way to hating,\n    And yet don’t look too good, nor talk too wise:"
		print "VERSE TWO"
		print "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;"
		print "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;"
		print "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
		print "Or watch the things you gave your life to, broken,\n    And stoop and build ’em up with worn-out tools:"
v2cont()

#### VERSE THREE ####

def v3i():
    print "\nVERSE THREE" 
    print "1. " + "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone,"  
    print "2. " + "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss," # 
    print "3. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
    print "4. " + "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;"
    v3i_choice = raw_input("What's the first phrase?\n1,2,3,4? ")
    if v3i_choice == "2":
    	print "Correct!\n"
    elif v3i_choice == "1" or "3" or "4":
    	print "Sorry, try again!"
    	v3i()
v3i()

def v3ii():
    print "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,..." 
    print "1. " + "And lose, and start again at your beginnings\n    And never breathe a word about your loss;" #  
    print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"  
    print "3. " + "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;"
    print "4. " + "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;  "
    v3ii_choice = raw_input("What's the second phrase?\n1,2,3,4? ")
    if v3ii_choice == "2":
    	print "Correct!\n"
    elif v3ii_choice == "1" or "3" or "4":
    	print "Sorry, try again!"
    	v3ii()
v3ii()

def v3iii():
    print "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,"
    print "And lose, and start again at your beginnings\n    And never breathe a word about your loss;..."
    print "1. " + "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;"
    print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
    print "3. " + "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone," #
    print "4. " + "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;"
    v3iii_choice = raw_input("What's the third phrase?\n1,2,3,4? ")
    if v3iii_choice == "3":
    	print "Correct!\n"
    elif v3iii_choice == "1" or "2" or "4":
    	print "Sorry, try again!"
    	v3iii()
v3iii()

def v3iv():
    print "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,"
    print "And lose, and start again at your beginnings\n    And never breathe a word about your loss;"
    print "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone,..."
    print "1. " + "Or watch the things you gave your life to, broken,\n    And stoop and build ’em up with worn-out tools:"  
    print "2. " + "And so hold on when there is nothing in you\n    Except the Will which says to them: ‘Hold on!’" # 
    print "3. " + "Or being hated, don’t give way to hating,\n    And yet don’t look too good, nor talk too wise:"
    print "4. " + "Yours is the Earth and everything that’s in it,\n    And—which is more—you\’ll be a Man, my son!"
    v3ii_choice = raw_input("What's the fourth phrase?\n1,2,3,4? ")
    if v3ii_choice == "2":
    	print "Correct!\n"
    elif v3ii_choice == "1" or "3" or "4":
    	print "Sorry, try again!"
    	v3ii()
v3iv()

def v3cont():
	print "You've completed the third verse! There is one left! Would you like to review your progress before continuing, just continue, or quit and save your progress?"
	beginv3 = raw_input("review/continue/quit:")
	if beginv3 == "quit":
		print "Until next time, %s! Don't forget to follow your progress in ex36Your_Score.txt" % name
		with open("ex36Your_Score.txt", mode='a') as file:
			file.write("\n%s 75%% complete at %s" % (name, datetime.datetime.now()))
		exit(0)
	elif beginv3 == "continue":
		print ""
	elif beginv3 == "review":	
		print "VERSE ONE\nIf you can keep your head when all about you\n    Are losing theirs and blaming it on you,"
		print "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;"
		print "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
		print "Or being hated, don’t give way to hating,\n    And yet don’t look too good, nor talk too wise:"
		print "VERSE TWO\n"
		print "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;"
		print "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;"
		print "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
		print "Or watch the things you gave your life to, broken,\n    And stoop and build ’em up with worn-out tools:"
		print "VERSE THREE\n"
		print "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,"
    	print "And lose, and start again at your beginnings\n    And never breathe a word about your loss;"
    	print "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone,"
    	print "And so hold on when there is nothing in you\n    Except the Will which says to them: ‘Hold on!’"
v3cont()

#### VERSE FOUR ####

def v4i():
    print "\n[FINAL] VERSE FOUR" 
    print "1. " + "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone,"  
    print "2. " + "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss," 
    print "3. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
    print "4. " + "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch," #
    v4i_choice = raw_input("What's the first phrase?\n1,2,3,4? ")
    if v4i_choice == "4":
    	print "Correct!\n"
    elif v4i_choice == "1" or "2" or "3":
    	print "Sorry, try again!"
    	v4i()
v4i()

def v4ii():
    print "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch,..." 
    print "1. " + "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;" # 
    print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"  
    print "3. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
    print "4. " + "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss," 
    v4ii_choice = raw_input("What's the second phrase?\n1,2,3,4? ")
    if v4ii_choice == "1":
    	print "Correct!\n"
    elif v4ii_choice == "2" or "3" or "4":
    	print "Sorry, try again!"
    	v4ii()
v4ii()

def v4iii():
    print "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch,"
    print "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;..."
    print "1. " + "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"  
    print "2. " + "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"  
    print "3. " + "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone, "
    print "4. " + "If you can fill the unforgiving minute\n    With sixty seconds’ worth of distance run," # 
    v4iii_choice = raw_input("What's the third phrase?\n1,2,3,4? ")
    if v4iii_choice == "4":
    	print "Correct!\n"
    elif v4iii_choice == "1" or "2" or "3":
    	print "Sorry, try again!"
    	v4iii()
v4iii()

def v4iv():
    print "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch,"
    print "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;"
    print "If you can fill the unforgiving minute\n    With sixty seconds’ worth of distance run,..."
    print "1. " + "And so hold on when there is nothing in you\n    Except the Will which says to them: ‘Hold on!’"
    print "2. " + "Yours is the Earth and everything that’s in it,\n    And—which is more—you’ll be a Man, my son!" #
    print "3. " + "And lose, and start again at your beginnings\n    And never breathe a word about your loss;"
    print "4. " + "Or watch the things you gave your life to, broken,\n    And stoop and build ’em up with worn-out tools:"
    v4iv_choice = raw_input("What's the fourth phrase?\n1,2,3,4? ")
    if v4iv_choice == "4":
    	print "Correct!\n"
    elif v4iv_choice == "1" or "2" or "3":
    	print "Sorry, try again!"
    	v4iv()
v4iv()

def v4end():
	print "You've completed the poem!! You're now done! You can review and quit, or just quit."
	beginv4 = raw_input("review/quit:")
	if beginv4 == "review":
		print "Until next time, %s! Don't forget to follow your progress in ex36Your_Score.txt" % name
		with open("ex36Your_Score.txt", mode='a') as file:
			file.write("\n%s 100%% complete at %s" % (name, datetime.datetime.now()))
		print "VERSE ONE\n"
		print "If you can keep your head when all about you\n    Are losing theirs and blaming it on you,"
		print "If you can trust yourself when all men doubt you,\n    But make allowance for their doubting too;"
		print "If you can wait and not be tired by waiting,\n    Or being lied about, don’t deal in lies,"
		print "Or being hated, don’t give way to hating,\n    And yet don’t look too good, nor talk too wise:"
		print "VERSE TWO\n"
		print "If you can dream—and not make dreams your master;\n    If you can think—and not make thoughts your aim;"
		print "If you can meet with Triumph and Disaster\n    And treat those two impostors just the same;"
		print "If you can bear to hear the truth you’ve spoken\n    Twisted by knaves to make a trap for fools,"
		print "Or watch the things you gave your life to, broken,\n    And stoop and build ’em up with worn-out tools:"
		print "VERSE THREE\n"
		print "If you can make one heap of all your winnings\n    And risk it on one turn of pitch-and-toss,"
		print "And lose, and start again at your beginnings\n    And never breathe a word about your loss;"
		print "If you can force your heart and nerve and sinew\n    To serve your turn long after they are gone,"
		print "And so hold on when there is nothing in you\n    Except the Will which says to them: ‘Hold on!’"
		print "VERSE FOUR\n"
		print "If you can talk with crowds and keep your virtue,\n    Or walk with Kings—nor lose the common touch,"
		print "If neither foes nor loving friends can hurt you,\n    If all men count with you, but none too much;"
		print "If you can fill the unforgiving minute\n    With sixty seconds’ worth of distance run,"
		print "Yours is the Earth and everything that’s in it,\n    And—which is more—you’ll be a Man, my son!"
		exit(0)
	elif beginv4 == "quit":
		print "Until next time, %s! Don't forget to follow your progress in ex36Your_Score.txt" % name
		with open("ex36Your_Score.txt", mode='a') as file:
			file.write("\n%s 100%% complete at %s" % (name, datetime.datetime.now()))
		exit(0)
v4end()