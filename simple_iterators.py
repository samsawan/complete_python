l = [1,2,3,4,5]

for num in l:
	if num % 2 == 0:
		print '{} is even'.format(num)
	else:
		print '{} is odd'.format(num)

sum = 0
for num in l:
	sum += num

print 'the sum is {}'.format(sum)

s = 'this is a string'
for char in s:
	print char

tup = (1,2,3,4,5)

for t in tup:
	print t

# tuple unpacking pretty cool erlang shit!
l = [(2,4), (6,8), (10,12)]
for (t1, t2) in l:
	print t2

# print the key only
d = {'k1':1, 'k2':2,'k3':3}
for item in d:
	print item

# unpacking the key/value
for k, v in d.iteritems():
	print 'the key is {}'.format(k)
	print 'the value is {}'.format(v)