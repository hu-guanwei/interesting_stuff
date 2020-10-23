from collections import defaultdict


class Node:

	def __init__(self, val, grad=[]):
		self.val = val
		self.grad = grad

	def __mul__(self, other):
		val = self.val * other.val
		grad = [(self, other.val), (other, self.val)]
		return Node(val, grad)

	def __add__(self, other):
		val = self.val + other.val
		grad = [(self, 1), (other, 1)]
		return Node(val, grad)

	def backward(self):
		g = defaultdict(lambda: 0)
		stack = self.grad.copy()

		while stack:
			node, grad_acc = stack.pop()
			g[node] += grad_acc
			
			for child_node, grad_local in node.grad:
				stack.append((child_node, grad_acc * grad_local))

		return g


if __name__ == '__main__':

	X = Node(10)
	Y = Node(39)
	Z = Node(77)
	W = X + Y * Z
	print(W.backward()[X])
	print(W.backward()[Y])
	print(W.backward()[Z])
