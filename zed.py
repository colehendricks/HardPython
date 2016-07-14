name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_CM = height * 2.54 #cm
weight_KG = weight * 0.454 #kg

print "Let's talk about %s." % name
print "He's %d inches tall." %  height
print "He's %d pounds heavy" % weight
print "Actually he's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usaully %s depending on the coffee." % teeth
print "His measurements in metric are %d cm and %d kg ." % (height_CM, weight_KG)

#Tricky line
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)