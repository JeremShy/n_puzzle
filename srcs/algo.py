# from srcs.globals import srcs.globals.g_hash_end_state
import srcs.globals

def	initialize_map(end_state):
	print (srcs.globals.g_hash_end_state)
	srcs.globals.g_hash_end_state = [1 for i in range (end_state.size * end_state.size)]
	for i in range(end_state.size):
		for j in range(end_state.size):
			srcs.globals.g_hash_end_state[end_state.state[i][j]] = (i, j)
	print (srcs.globals.g_hash_end_state)

def solve(initial_state, end_state):
	initialize_map(end_state)
	print (initial_state.manhattanDistance())
