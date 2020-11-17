from random import uniform
from functools import reduce, partial

n_trials = 10000000
r = partial(uniform, -1, 1)
seq = range(n_trials)
n_hits = reduce(lambda x, y: x + y, map(lambda x: int(r()**2 + r()**2 <= 1), seq))

print(4 * n_hits / n_trials)


from time import time
from statistics import mean, stdev

def log(n):
	def inner(func):
		def wrapper(*args, **kwargs):
			results = [func(*args, **kwargs) for _ in range(n)]
			return (mean(results), stdev(results))
		return wrapper
	return inner

		
f = lambda _: 4 * int(r()**2 + r()**2 <= 1)
f = log(n_trials)(f)
print(f(None))


from math import sqrt
from random import random

g = lambda _: 4 * sqrt(1 - random()**2)
g = log(n_trials)(g)
print(g(None))

def h():
	x = random() 
	return 2 * (sqrt(1 - x**2) + sqrt(1 - (1 - x)**2))

def k():
	res = 0
	x = random()
	y = random()
	res += (x ** 2 + y ** 2) <= 1
	res += ((1 - x) ** 2 + (1 - y) ** 2) <= 1 
	res += (x ** 2 + (1 - y) ** 2) <= 1
	res += ((1 - x) ** 2 + y ** 2) <= 1
	return res

h = log(n_trials)(h)
print(h())


k = log(n_trials)(k)
print(k())

