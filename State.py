from random import shuffle
import re
#from srcs.globals import g_hash_end_state

class State:
	def __generateRandom(self, size):
		listeuh = [i for i in range(size * size)]
		shuffle(listeuh)

		for i in range(size):
			tmp = []
			for j in range(size):
				tmp.append(listeuh.pop())
			self.state.append(tmp)

	def __parseFirstLine(self, listeuh):
		print("In first line")
		if len(listeuh) != 1:
			raise NPuzzleError("Invalid first line")
		number = int(listeuh[0])
		if number < 3:
			raise NPuzzleError("The size of the puzzle can't be lower than 3")
		return (number)

	def __parseOtherLine(self, listeuh):
		print("In other line")
		if len(listeuh) != self.size:
			raise NPuzzleError("Invalid line in file")
		temp = [int(i) for i in listeuh]
		self.state.append(temp)
		print (temp)

	def __parseFile(self, filename):
		print ("Parsing file : " + filename)
		firstTime = True
		file = open(filename, "r")
		for line in file:
			handled = line
			regex = re.compile(r'\#.*', re.DOTALL)
			handled = re.sub(regex, '', handled)
			handled = handled.strip()
			if not handled:
				continue
			temp = handled.split()
			print (temp)
			try:
				if firstTime == True:
					self.size = self.__parseFirstLine(temp)
					lineNumber = 0
					firstTime = False
				else:
					self.__parseOtherLine(temp)
					lineNumber += 1
					if lineNumber > self.size:
						raise NPuzzleError("Invalid number of lines in file")
			except ValueError as e:
				raise NPuzzleError("Error while parsing a line : Please enter only valid numbers")
		if lineNumber != self.size:
			raise NPuzzleError("Invalid nuber of lines in file")

	def __isValid(self):
		hashmap = [0 for i in range(self.size * self.size)]
		for line in self.state:
			for number in line:
				if number < 0 or number >= self.size * self.size:
					return (False)
				elif hashmap[number] == 0:
					hashmap[number] = 1
				else:
					return (False)

	def __str__(self):
		ret = ""
		for i in self.state:
			ret += str(i) + "\n"
		return ret

	def __init__(self, *args, **kwargs):
		self.state = []
		if ("file" in kwargs):
			print ("We need to parse the file " + kwargs["file"])
			self.__parseFile(kwargs["file"])
			if self.__isValid() == False:
				raise NPuzzleError("Invalid map.")
		elif ("size" in kwargs):
			print ("We need to generate a NxN puzzle with N=" + str(kwargs["size"]))
			if (kwargs["size"] < 3):
				raise NPuzzleError("Can't generate a puzzle with size lower than 3.")
			self.__generateRandom(kwargs["size"])
			self.size = int(kwargs["size"])
		elif ("liste" in kwargs):
			self.state = kwargs["liste"]
			self.size = len(kwargs["liste"])
		else:
			raise NPuzzleError("You must specify a 'file' or 'size' argument.")

