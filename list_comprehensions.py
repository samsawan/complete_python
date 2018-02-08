# one line for loop

l = []

for letter in 'word':
	l.append(letter)

print l

l2 = [ letter for letter in 'word' ]

print l2
print l2 == l

# square every number
lst = [ num ** 2 for num in xrange(6) ]
print lst

# even number checker
lst = [ num for num in xrange(11) if num % 2 == 0 ]
print lst

cel_list = [0, 10, 20.1, 34.5]
farh_list = [ temp * (9/5.0) + 32 for temp in cel_list ]
print farh_list

# nested list comprhension
# for all numbers 0 - 10, square them then divide by 2
# take note of the scoping!
lst = [ num / 2.0 for num in [ num ** 2 for num in xrange(11) ] ]
print lst