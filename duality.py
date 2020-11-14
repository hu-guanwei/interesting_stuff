#!usr/bin/python3

class Adder:
	def __init__(self, z):
		self.z = z

	def __call__(self, x, y):
		self.z += 1
		print(f'it has been called {self.z} times')
		return x + y


def add(z):
	def wrapper(x, y):
		nonlocal z
		z += 1
		print(f'it has been called {z} times')
		return x + y
	return wrapper


add1 = add(0)
add2 = Adder(0)

print(add1(1, 2))
print(add2(1, 2))

print(add1(1, 2))
print(add2(1, 2))
