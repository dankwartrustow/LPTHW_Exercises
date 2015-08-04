print """You enter a dark room with two doors. 
Do you go through blue door #1 or red door #2 with a light over it? 
3. You also see a window. 
4. You see a rank ass THOT who owe you 20."""

act = raw_input("> ")

if act == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
    	print "The bear eats your legs off. Good job!"
    else: 
    	print "Well, doing %s is probably better. Bear runs away." % bear

elif act == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else: 
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif act == "3":
	print """You walk up to the window, peek outside and see the beautiful moon.
	Just as you seem to find peace, you feel a heavy thud behind your shoulder blades. 
    The grass is rushing to meet you. You can see the moon reflecting off the dew,
    shining with the intensity of your last heart beats. Good job!"""

elif act == "4":
	print "You pop a cap or two, go home the boss."
	print "Girl's homies know whatsup. You're wanted in the hood now and cops know too."
	print "1. Pop a cap at the police. Ain't no place in heaven for a gangsta."
	print "2. Pop caps at the homies, don't matter how many of them are."
	print "3. Run and lose all your rep in the hood."

	choice = raw_input("nig??")

	if choice == "1":
		print "Damn, now you locked up and got the death penalty! You fucked."
	elif choice == "2":
		print "Damn, now you dead as shit all holey and all yo."
	elif choice == "3":
		print "Damn, now you can't come back and gotta integrate with white people."
	else:
		print "Well I guess %s seemed like a good choice, but THOT as bitches never die."

else: 
    print "You stumble around and foll on a knife and die. Good job!"
