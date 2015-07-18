# Made a mistake: forgot to put quotes around the formatters on line 2
# IMPORTANT: remember to only use %r for DEBUGGING and %s for strings
# Note: %r can be used for non-ASCII characters as well
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.", 
	"But it didn't sing.",
	"So I said goodnight."
	)