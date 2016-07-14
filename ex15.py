from sys import argv
#imports the module argv from sys to get
# user input for the following to variables

script, filename = argv
#populates variables for argv


txt = open(filename)
#defines txt as opening the file called in argv

print "Here is your file %r:" % filename
print txt.read()
#prints what is read in txt(argv(filename))

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()