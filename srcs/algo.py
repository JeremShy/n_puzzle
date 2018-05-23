# from srcs.globals import srcs.globals.g_hash_end_state
import srcs.globals
from queue import PriorityQueue
from queue import Queue

def	initialize_map(end_state):
	# print (srcs.globals.g_hash_end_state)
	srcs.globals.g_hash_end_state = [1 for i in range (end_state.size * end_state.size)]
	for i in range(end_state.size):
		for j in range(end_state.size):
			srcs.globals.g_hash_end_state[end_state.state[i][j]] = (i, j)
	# print (srcs.globals.g_hash_end_state)

def get_lowest_f(liste):
	min_val = -1
	for elem in liste:
		if (min_val == -1 or elem.g + elem.heuristique <= min_val):
			min_val = elem.g + elem.heuristique
			min_elem = elem
	liste.remove(min_elem)
	# print ("min : " + str(min_val))
	return min_elem

def countain(liste, to_check):
	for elem in liste:0
		if elem.state == to_check.state:
			return elem
	return False

def countain_pq(liste, to_check):
	for heuristique, elem in liste.queue:
		if elem.state == to_check.state:
			return elem
	return False

def solve(initial_state, end_state):
	initialize_map(end_state)
	initial_state.calcHeuristique()
	print ("initial_state : " + str(initial_state.heuristique))

	end_state.calcHeuristique()
	print ("end_state : " + str(end_state.heuristique))

	openset = PriorityQueue()

	openset.put_nowait((initial_state.heuristique + initial_state.g, initial_state))
		closedset = {}

	while (openset):
		current_heur, current = openset.get_nowait()
		closedset[str(current.state)] = 1
		
		if (current.heuristique == 0):
			print("Is ok")
			print (current)
			print (current.g)
			return True
		neighbors = current.getNeighbors()
		if (not neighbors):			
			continue
		for neighbor in neighbors:
			if str(neighbor.state) in closedset:
				continue
			tmp = countain_pq(openset, neighbor)
			if (tmp == False):
				pouet = (neighbor.heuristique + neighbor.g, neighbor)
				openset.put_nowait(pouet)
			else:
				if (tmp.g > neighbor.g):
					# print ("replacing " + str(tmp.heuristique + tmp.g) + "with" + str(neighbor.heuristique + neighbor.g))
					tmp.g = neighbor.g
					# TODO predecesseur

