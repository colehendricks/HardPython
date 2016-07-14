

#user_input = raw_input(">")


	
def populate_list(l):
	i = 0
	numbers = []
	while i < l:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i +1
	
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	

	print "The numbers:"

	for num in numbers:
		print num

l = 8
list = populate_list(l)


print "The list contains the following: %r" % list	
