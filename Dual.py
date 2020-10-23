# simple implementation of forward mode of autodiff
# using dual number algebra

DUAL_RULES = {
	'add': lambda x, y: Dual(x.val + y.val, x.dot + y.dot),
	'sub': lambda x, y: Dual(x.val - y.val, x.dot - y.dot),
	'mul': lambda x, y: Dual(x.val * y.val, x.val * y.dot + x.dot * y.val)
} # TODO: add 'div'


class Dual:

	def __init__(self, val, dot=0):
		self.val = val
		self.dot = dot

	def __repr__(self):
		return '{} + {} eps'.format(self.val, self.dot)

	__add__, __sub__, __mul__ = DUAL_RULES['add'], DUAL_RULES['sub'], DUAL_RULES['mul']


def dual_log(d):
	from math import log
	return Dual(log(d.val), d.dot / d.val)


if __name__ == '__main__':

	x = Dual(10, 1)
	y = Dual(37)
	z = Dual(4.2)
	f = dual_log(x * y + z)

	'''
	[x]  [y]
     \   /
       *
      [a]   [z]
        \   /
          +
         [f]
	'''

	print(f'{f}')
	print(y.val / (x.val * y.val + z.val))

