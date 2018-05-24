# from srcs.globals import srcs.globals.g_hash_end_state
import srcs.globals
from queue import PriorityQueue
from queue import Queue
from srcs.State import State

def	initialize_map(end_state):
	# print (srcs.globals.g_hash_end_state)
	srcs.globals.g_hash_end_state = [1 for i in range (end_state.size * end_state.size)]
	for i in range(end_state.size):
		for j in range(end_state.size):
			srcs.globals.g_hash_end_state[end_state.state[i][j]] = (i, j)
	# print (srcs.globals.g_hash_end_state)

def countain_pq(liste, to_check):
	if (to_check.heuristique + to_check.g, to_check) in liste.queue:
		return liste.queue.index((to_check.heuristique + to_check.g, to_check))
	else:
		return False

def solve(initial_state, end_state):
	initialize_map(end_state)
	initial_state.calcHeuristique()

	initial_state.predecesseur = False

	end_state.calcHeuristique()

	openset = PriorityQueue()

	openset.put((initial_state.heuristique + initial_state.g, initial_state))
	closedset = {}

	total_number_selected_in_openset = 1

	while (not openset.empty()):
		current_heur, current = openset.get()
		closedset[str(current.state)] = 1

		if (current.state == end_state.state):
			print ("Total number of states ever selected in the \"opened\" set: " + str(total_number_selected_in_openset))
			print ("Maximum number of states ever represented in memory at the same time during the search: " + str(State.max_numbers))
			print ("Number of moves required to transition from the initial state to the final state: " + str(current.g) + "\n")
			x = ""
			while current != False:
				x = str(current) + "\n" + x
				current = current.predecesseur
			print (x, end="")
			return True
		neighbors = current.getNeighbors()
		# print (current)
		if neighbors:
			for neighbor in neighbors:
				neighbor.predecesseur = current
				if not str(neighbor.state) in closedset:
					tmp = countain_pq(openset, neighbor)
					if (tmp == False):
						openset.put((neighbor.heuristique + neighbor.g, neighbor))
						total_number_selected_in_openset += 1
					else:
						if (openset.queue[tmp][1].g > neighbor.g):
							openset.queue[tmp][1].g = neighbor.g
							print ("a")
							openset.queue[tmp][1].predecesseur = neighbor.predecesseur
