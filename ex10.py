# '\t' creates a tab
tabby_cat = "\tI'm tabbed in."
# '\n' splits a line
persian_cat = "I'm split\non a line."
# '\\' escapes the 2nd backslash to become visible in the string
backlash_cat = "I'm \\ a \\ cat."

# """ starts the ability to create a multi-line string
# \t tabs a line over while "*" is simply part of the string although confusing
# Zed mixes it up on the Catnip line to show you can use '\n' even within """
fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# prints the abovementioned variables
print tabby_cat
print persian_cat
print backlash_cat
print fat_cat


# STUDY DRILL SECTION

test1 = ''' sexy little hoes
be all totes \t mcgotes \n like yo'''
test2 = """ can't you\n tell\t me\n the\t meaning of\n the US Constitution """

print "lfnd;lkf %r lfnd;alkf" % test1
print ";lfdna;lfknda %s lfnd;alknfa" % test2