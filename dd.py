from numpy import random, array, dot
from numpy.linalg import norm

class DD(object):
	"""docstring for DD"""
	net = []
	def __init__(self, arg):
		super(DD, self).__init__()
		self.arg = arg
		net = random.rand(2,2); l = 1

	def forward(_inp): return [activation(dot(_inp, net[j])) for j in range(0, 2)]

	def bp(_inps): for q in range(0, len(_inps)): net += [[l * (_inps[q][1 - k]-_inps[q][k]) * pow(-1, j)  for k in (0, 1)] for j in (0, 1)]
		
	def activation(x): return 1 / 1 + exp(-x)
