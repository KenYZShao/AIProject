#Utility function to make 6x6 SUDOKU board, helper class and variables

import queue
import time
from copy import deepcopy

def cross(A,B):
	return [a + b for a in A for b in B]

digits = "123456"
rows = "ABCDEF"
cols = digits
squares = cross(rows, cols)

class Sudoku:

	#Initialize the Sudoku class
	def __init__ (self, domain = digits, grid = ""):
		self.varibales = squares
		self.domain = self.returnDict(grid)
		self.values = self.returnDict(grid)

		self.unitlist = ([cross(rows,c) for c in cols] + 
							[cross(r,cols) for r in rows] + 
							[cross(rs, cs) for rs in ('ABC', 'DEF') for cs in ('123', '456')])

		self.units = dict((s, [u for u in self.unitlist if s in u]) for s in squares)
		self.peers = dict((s, set(sum(self.units[s],[]))-set([s])) for s in squares)
		self.constraints = {(varibales, peers) for varibales in self.varibales for peers in self.peers[varibales]}

	def returnDict(self, grid=""):
		x = 0
		game = dict()
		for value in self.varibales:
			if grid[x]!='0':
				game[value] = grid[x]
			else:
				game[value] = digits
			x = x + 1
		return game