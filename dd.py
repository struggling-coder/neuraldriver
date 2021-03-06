from numpy import random, array, dot, exp
from numpy.linalg import norm

class DD(object):

	def __init__(self):
		super(DD, self).__init__()
		self.net = random.rand(2,2); l = 1
	
	def activation(self, x): return 1 / (1 + exp(-x))

	def forward(self, _inp): return [self.activation(dot(array(_inp), self.net[j])) for j in range(0, 2)]

	def bp(self, _inps): 
		for q in range(0, len(_inps)): self.net += array([[l * (_inps[q][1 - k]-_inps[q][k]) * pow(-1, j)  for k in (0, 1)] for j in (0, 1)])
