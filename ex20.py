from sys import argv
#imports the argv function

script, input_file = argv
#defines the arguments to input at argv

def print_all(f):
#define the print all function and its argument name: f
	print f.read()
	#defines what print all does: reads and prints f(current file)
	
def rewind(f):
	f.seek(0)
	#rewinds f(current file)
	
def print_a_line(line_count, f):
	print line_count, f.readline()
	
current_file = open(input_file)
#makes input file open and 'current file'

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line =+ 1
print_a_line(current_line, current_file)

Current_line =+ 1
print_a_line(current_line, current_file)
