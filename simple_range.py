print range(10)
print range(10) == range(0,10)

# step size of two
print range(0, 20, 2)

# range generates a list of numbers saved in memory
# xrange is lazy evaluation

for num in xrange(1,6):
	print num

x = xrange(1,6)
x2 = range(1,6)

print type(x), type(x2)

x3 = list(x)
print type(x2) == type(x3)