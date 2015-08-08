from sys import exit

# Refactored ordering of code to better match game's order of operations.

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if "left" in next:
        bear_room()
    elif "right" in next:
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

# Refactored bear_room if statements to better match cthulhu if statements.
# The difference is in having to receive exact statements for raw_input, as opposed to simply
# checking if code contains certain keywords. Much better experience for user, and less annoyance since
# there are no options. Also better to hint to the user they can scare/taunt the bear, otherwise it's
# a trick question with little to no resolution.

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey, and looks like he might be scared of you... might."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    # issues with this block of code, using ("text" in variable and variable) within an elif
    # need to figure out how to recognize non-binary contextual responses, will leave this broken for now
    while True:
        next = raw_input("> ")
        # bear_moved = False
        if "honey" in next:
            dead("The bear looks at you then slaps your face off.")
        elif not bear_moved and "taunt" or "surprise" or "yell" or "scare" in next:
            bear_moved = True
            print "The bear has moved from the door. You can go through it now."
        elif bear_moved and "taunt" or "surprise" or "yell" or "scare" in next:
            dead("The bear gets pissed off and chews your leg off.")
        elif bear_moved and next == "open door":
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next: 
        start()
    elif "head" or "eat" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def gold_room():
    print "This room is full of gold. How much do you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

start()
