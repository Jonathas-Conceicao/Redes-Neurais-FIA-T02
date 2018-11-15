from random import uniform, random

def sign(n): return 1 if n > 0 else -1

def habbsrule(weight, rate, a, b):
	return float('%.4f' % (weight + rate*a*b))

class perceptron:
	def __init__(self, length, rate):
		# weights = [float('%.4f' % random()) for _ in range(0, length)]
		weights = [float('%.4f' % uniform(-1, 1)) for _ in range(0, length)]
		self.weights = weights
		self.length = length
		self.epocas = 0
		self.learnRate = rate
		pass

	def getWeights(self):   return self.weights
	def getEpocas(self):    return self.epocas
	def getLearnRate(self): return self.learnRate

	def train(self, data, expected):
		for (sd, se) in zip(data, expected):
			self.updateWeight(sd, se)
		return

	def calculate(self, sData):
		vs = [(lambda x, y: x * y)(a, b) for (a, b) in zip(sData, self.weights)]
		# return sum(vs)/sum(self.weights)
		return sign(sum(vs)/sum(self.weights))

	def calculateAll(self, data):
		return [self.calculate(d) for d in data]

	def updateWeight(self, sData, sExpected):
		self.epocas += 1
		print "for ", sData, ": ", sExpected, " <> ", self.calculate(sData)
		self.weights = [habbsrule(w, self.learnRate, self.calculate(sData), sExpected)
										for w in self.weights]
		return
	pass

def parseInput(fn):
	i = []
	d = []
	with open(fn) as f:
		lines = f.readlines()
		lines.pop(0) # header
		for line in lines:
			args, expected = parseLine(line)
			i.append(args)
			d.append(expected)
			pass
		pass
	return (i, d)

def parseLine(line):
	w = filter(None, line.split(' '))
	args = []
	for i in range(0, len(w) - 1):
		args.append(float(w[i]))
		pass
	return (args, int(float(w[-1])))

# test
t = perceptron(3, 0.01)
print 'Pesos pre treinamento: ', t.getWeights()
(datas, desireds) = parseInput('res/anexo1.txt')
t.train (datas, desireds)
print 'Pesos pos treinamento: ', t.getWeights()
print 'In : ', desireds
print 'Out: ', t.calculateAll(datas)
