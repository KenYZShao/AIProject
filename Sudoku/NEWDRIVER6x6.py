import queue
import time
from copy import deepcopy

def cross(A,B):
	return [a + b for a in A for b in B]


# def choose_Dimenion(size_n=""):
# 	dim = (size_n)
# 	if (dim == "6"):
# 		digits = "123456"
# 		rows = "ABCDEF"
# 		cols = digits
# 		squares = cross(rows, cols)
# 	else:
# 		digits = "123456789"
# 		rows = "ABCDEFGHI"
# 		cols = digits
# 		squares = cross(rows, cols)

digits = "123456"
rows = "ABCDEF"
cols = digits
squares = cross(rows, cols)

class Sudoku:

	# choose_Dimenion(dim_size)
	def __init__ (self, domain = digits, grid = ""):
		# choose_Dimenion(dim_size)
		self.varibales = squares
		self.domain = self.returnDict(grid)
		self.values = self.returnDict(grid)

		# if (dim_size == "6"):
		# 	self.unitlist = ([cross(rows,c) for c in cols] + 
		# 					 [cross(r,cols) for r in rows] + 
		# 					 [cross(rs, cs) for rs in ('ABC', 'DEF') for cs in ('123', '456')])
		# else :
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


def AC3(Sudoku):
	q = queue.Queue()

	for arc in Sudoku.constraints:
		q.put(arc)

	i = 0
	while not q.empty():
		(Xi, Xj) = q.get()

		i = i + 1

		if ReviseAC3(Sudoku, Xi, Xj):
			if len(Sudoku.values[Xi]) == 0:
				return False

			for Xk in (Sudoku.peers[Xi] - set(Xj)):
				q.put((Xk, Xi))
	return True

def ReviseAC3(Sudoku, Xi, Xj):
	isRevised = False
	values = set(Sudoku.values[Xi])

	for x in values:
		if not isconsistentAC3(Sudoku, x, Xi, Xj):
			Sudoku.values[Xi] = Sudoku.values[Xi].replace(x, '')
			isRevised = True
			
	return isRevised

def isconsistentAC3(Sudoku, x, Xi, Xj):
	for y in Sudoku.values[Xj]:
		if Xj in Sudoku.peers[Xi] and y!=x:
			return True
	return False

def display(values):
	for r in rows:
		if r in 'DG':
			print("-----------------------------------------------------------")
		for c in cols:
			if c in '47':
				print (' | ', values[r+c], ' ',end=' ')
			else:
				print(values[r+c], ' ',end=' ')
		print(end='\n')

def isCompleteAC3(Sudoku):
	for variables in squares:
		if len(Sudoku.values[variables])>1:
			return False
	return True


def write(values):
	solves_sudoku = ""
	for variables in squares:
		solves_sudoku = solves_sudoku + values[variables]
	return solves_sudoku


def Backtracking_Search(Sudoku):
	return Recursive_Backtracking({}, Sudoku)

def Recursive_Backtracking(assignment, Sudoku):
	if isComplete(assignment):
		return assignment
	var = Select_Unassigned_Variables(assignment, Sudoku)
	domain = deepcopy(Sudoku.values)

	for value in Sudoku.values[var]:
		if isConsistent(var, value, assignment, Sudoku):
			assignment[var] = value
			state = {}
			state = forward_check(assignment, state, Sudoku, var, value)
			if state!= "NOT SOLVED":
				results = Recursive_Backtracking(assignment, Sudoku)
				if results!= "NOT SOLVED":
					return results

			del assignment[var]
			Sudoku.values.update(domain)

	return "NOT SOLVED"

def forward_check(assignment, state, Sudoku, var, values):
	state[var] = values
	for neighbour in Sudoku.peers[var]:
		if neighbour not in assignment and values in Sudoku.values[neighbour]:
			if len(Sudoku.values[neighbour])==1:
				return "NOT SOLVED"

			remaining = Sudoku.values[neighbour] = Sudoku.values[neighbour].replace(values,"")

			if len(remaining)==1:
				result = forward_check(assignment, state, Sudoku, neighbour, remaining)
				if result== "NOT SOLVED":
					return "NOT SOLVED"
	return state

def isComplete(assignment):
	return set(assignment.keys())==set(squares)

def Select_Unassigned_Variables(assignment, Sudoku):
	unassigned_Variables = dict((squares, len(Sudoku.values[squares])) for squares in Sudoku.values if squares not in assignment.keys())
	mrv = min(unassigned_Variables, key=unassigned_Variables.get)
	return mrv

def isConsistent(var, values, assignment, Sudoku):
	for neighbour in Sudoku.peers[var]:
		if neighbour in assignment.keys() and assignment[neighbour]==values:
			return False
	return True

