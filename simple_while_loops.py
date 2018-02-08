x = 0
while x < 10:
	print 'x is currently ', x
	x += 1

x = 0
while x < 10:
	print 'x is currently ', x
	x += 1

# final thing that gets run when the while loop is done running
else:
	print 'All done'

x = 0
while x < 10:
	print 'x is currently ', x
	print 'x is still less, adding one'

	x += 1
	if x == 3:
		print 'hey neat x equals 3'
		# this will stop the execution of the outer loop
		# break
	else:
		print 'continuing...'
		# kinda not necessary
		continue