from random import shuffle
import re
import functools
from copy import deepcopy
#from srcs.globals import g_hash_end_state
# from srcs.globals import g_hash_end_state

import srcs.globals

class State:
	def __lt__(self, other):
		return (0)

	def __generateRandom(self, size):
		listeuh = [i for i in range(size * size)]
		shuffle(listeuh)

		for i in range(size):
			tmp = []
			for j in range(size):
				tmp.append(listeuh.pop())
			self.state.append(tmp)

	def __parseFirstLine(self, listeuh):
		# print("In first line")
		if len(listeuh) != 1:
			raise NPuzzleError("Invalid first line")
		number = int(listeuh[0])
		if number < 3:
			raise NPuzzleError("The size of the puzzle can't be lower than 3")
		return (number)
	
	def __parseOtherLine(self, listeuh):
		# print("In other line")
		if len(listeuh) != self.size:
			raise NPuzzleError("Invalid line in file")
		temp = [int(i) for i in listeuh]
		self.state.append(temp)
		# print (temp)

	def __parseFile(self, filename):
		# print ("Parsing file : " + filename)
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
			# print (temp)
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

	def manhattanDistance(self):
		global g_hash_end_state
		# print (srcs.globals.g_hash_end_state)
		acc = 0
		for i in range (self.size * self.size):
			 acc += abs(i % self.size - srcs.globals.g_hash_end_state[self.state[i % self.size][i // self.size]][0]) + abs(i // self.size - srcs.globals.g_hash_end_state[self.state[i % self.size][i // self.size]][1])
		return acc

	def calcHeuristique(self):
		global g_hash_end_state
		if (srcs.globals.g_hash_end_state != []):
			self.heuristique = self.manhattanDistance()
	
	def canMoveUp(self):
		for y in range(self.size):
			for x in range(self.size):
				if (self.state[y][x] == 0):
					if (y == 0):
						return False
					else:
						return True
	
	def getMovedUp(self):
		copy = State(state=self)
		for y in range(copy.size):
			for x in range(copy.size):
				if (copy.state[y][x] == 0):
					tmp = copy.state[y - 1][x]
					copy.state[y - 1][x] = copy.state[y][x]
					copy.state[y][x] = tmp
					copy.calcHeuristique()
					return copy

	def canMoveDown(self):
		for y in range(self.size):
			for x in range(self.size):
				if (self.state[y][x] == 0):
					if (y == self.size - 1):
						return False
					else:
						return True
	
	def getMovedDown(self):
		copy = State(state=self)
		for y in range(copy.size):
			for x in range(copy.size):
				if (copy.state[y][x] == 0):
					tmp = copy.state[y + 1][x]
					copy.state[y + 1][x] = copy.state[y][x]
					copy.state[y][x] = tmp
					copy.calcHeuristique()
					return copy

	def canMoveLeft(self):
		for y in range(self.size):
			for x in range(self.size):
				if (self.state[y][x] == 0):
					if (x == 0):
						return False
					else:
						return True
	
	def getMovedLeft(self):
		copy = State(state=self)
		for y in range(copy.size):
			for x in range(copy.size):
				if (copy.state[y][x] == 0):
					tmp = copy.state[y][x - 1]
					copy.state[y][x - 1] = copy.state[y][x]
					copy.state[y][x] = tmp
					copy.calcHeuristique()
					return copy

	def canMoveRight(self):
		for y in range(self.size):
			for x in range(self.size):
				if (self.state[y][x] == 0):
					if (x == self.size - 1):
						return False
					else:
						return True
	
	def getMovedRight(self):
		copy = State(state=self)
		# print ("Init")
		# print(copy)
		for y in range(copy.size):
			for x in range(copy.size):
				if (copy.state[y][x] == 0):
					tmp = copy.state[y][x + 1]
					copy.state[y][x + 1] = copy.state[y][x]
					copy.state[y][x] = tmp
					copy.calcHeuristique()
					# print ("copy")
					# print (copy)
					return copy

	def getNeighbors(self):
		ret = []
		if (self.canMoveUp() == True):
			ret.append(self.getMovedUp())
		if (self.canMoveDown() == True):
			ret.append(self.getMovedDown())
		if (self.canMoveLeft() == True):
			ret.append(self.getMovedLeft())
		if (self.canMoveRight() == True):
			ret.append(self.getMovedRight())
		return (ret)

	def __init__(self, *args, **kwargs):
		self.state = []
		if ("file" in kwargs):
			# print ("We need to parse the file " + kwargs["file"])
			self.__parseFile(kwargs["file"])
			if self.__isValid() == False:
				raise NPuzzleError("Invalid map.")
		elif ("size" in kwargs):
			# print ("We need to generate a NxN puzzle with N=" + str(kwargs["size"]))
			if (kwargs["size"] < 3):
				raise NPuzzleError("Can't generate a puzzle with size lower than 3.")
			self.__generateRandom(kwargs["size"])
			self.size = int(kwargs["size"])
		elif ("liste" in kwargs):
			self.state = deepcopy(kwargs["liste"])
			self.size = len(kwargs["liste"])
		elif ("state" in kwargs):
			self.state = deepcopy(kwargs["state"].state)
			self.size = kwargs["state"].size
			self.heuristique = kwargs["state"].heuristique
			self.g = kwargs["state"].g + 1
			return ;
		else:
			raise NPuzzleError("You must specify a 'file' or 'size' argument.")
		self.calcHeuristique()
		self.g = 0

