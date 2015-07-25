# This function uses the split method to create an array? of all the words, 
# separating them where this is a single space.
def break_words(stuff):
   """This funciton will break up words for us."""
   words = stuff.split(' ')
   return words

# Does not matter that the argument inside the function is 'words'. 
# in the example, he creates a variable called 'words' to keep it standard.
# Illustrates performing this function after split()
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

# Appears to go to byte 0 of the parameter.
# Notice that 'running words.pop(0)' allows it to retain the result of
# the comand. As it's part of the funciton, this occurs each time it is called
# and (it appears) within the function, retains that state until its end. It
# is cyclical, as pop(0) is done within the function. If external, seems
# it would be different.
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

# Appears to go to the last byte of the parameter. No fucking clue
# how -1 accomplishes that just yet...
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

# Is able to call the first two functions (above). Creates a variable for
# 'break_words' and uses initial 'sentence' argument. Then, calls 
# 'sort_words' function while using (duplicate) instance variable 'words'.
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

# Notice the 'words' variable being created again. Remember to not confuse the
# inability to instantiate a function/instance variable with the ability to
# instantiate a function within another funciton, and in the script.
# Learning to think in these deliberately iterative steps may be difficult. 
# I think I'd just try to do it all at once, while it may be easier to just
# break it apart into recallable pieces as shown here. 
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

# Note that using 'help(imported python file)' allows you to generate
# help file. This uses the """x """ to create a 'comment' that will be used
# only by the help file. This may prove more useful to express the code's
# purpose to a dev, while leaving comments to observations about the 
# overall direction the codebase is going, or needed fixes. This method
# appears to allow you to begin to make your own libraries, call them, 
# and also see an abbreviated list of the functions and their purpose.
# One more thing, note that performing this will create a python_script.pyc
# file in your folder (unmentioned by Zed). You can then call this from bash
# in the future just by typing 'pydoc python_script'! Super efficient.
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
