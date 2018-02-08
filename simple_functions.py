def my_addition_func(arg1, arg2):
	"""
	here is the docstring
	it's a good idea to use these
	"""
	print arg1 + arg2

# my_addition_func(1, 2)

def greeting(name):
	print 'hello {}!'.format(name)

greeting('Sam')

def add_num(num1, num2):
	return num1 + num2

x = add_num(1, 2)
# print x
x = add_num('first', 'second')
# print x

def is_prime(num):
	"""
	checks for prime numbers
	"""
	for n in xrange(2, num):
		if num % n == 0:
			print 'Not prime'
			break
	print 'Prime'

is_prime(13)
is_prime(12)
