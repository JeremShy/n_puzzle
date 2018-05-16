from random import shuffle

class State:
	def generateRandom(self, size):
		listeuh = [i for i in range(size * size)]
		shuffle(listeuh)

		self.state = []
		for i in range(size):
			tmp = []
			for j in range(size):
				tmp.append(listeuh.pop())
			self.state.append(tmp)
		print (self.state)

	def parseFile(self, filename):
		print ("Parsing file : " + filename)

	def __init__(self, *args, **kwargs):
		if ("file" in kwargs):
			print ("We need to parse the file " + kwargs["file"])
			self.parseFile(kwargs["file"])
		elif ("size" in kwargs):
			print ("We need to generate a NxN puzzle with N=" + str(kwargs["size"]))
			if (kwargs["size"] < 3):
				raise ValueError("Can't generate a puzzle with size lower than 3.")
			self.generateRandom(kwargs["size"])
		else:
			raise ValueError("You must specify a 'file' or 'size' argument.")

