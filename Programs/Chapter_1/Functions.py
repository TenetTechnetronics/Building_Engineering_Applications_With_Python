# Without arguments
def sayHello():
	print('Hello! ')

sayHello()  # Calling function without arguments

# With arguments
def sayHelloByName(name):
	print('Hello '+name +'!')

sayHelloByName('Rob') 	# Calling function with arguments


# Optional arguments
def sayHelloByOptionalName(name = 'Kane'):
	print('Hello '+name +'!')

sayHelloByOptionalName() 	# Calling function by optional arguments
