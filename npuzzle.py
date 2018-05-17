#!/usr/bin/env python3

import argparse
import sys
from State import State
from NPuzzleError import NPuzzleError

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-f", "--file", help="Specify an initial state of the puzzle.")
	group.add_argument("-s", "--size", type=int, help="Specify the size of a puzzle to generate.")
	args = parser.parse_args()

	if args.file is None and args.size is None:
		print (sys.argv[0] + ": You must specify a puzzle acquirement method.")
		sys.exit(1)

	try:
		if args.file:
			print ("File to read : " + args.file)
			initial_state = State(file=args.file)
		else:
			print ("The puzzle will be randomly generated")
			initial_state = State(size=args.size)
	except ValueError as e:
		print (str(e))
	except NPuzzleError as e:
		print (str(e))
	except IOError as e:
		print("An error occured : " + str(e))
