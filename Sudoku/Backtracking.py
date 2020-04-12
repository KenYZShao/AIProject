from Utilities import *
import queue
import time
from copy import deepcopy

def isConsistent(var, values, assignment, Sudoku):
	for neighbour in Sudoku.peers[var]:
		if neighbour in assignment.keys() and assignment[neighbour]==values:
			return False
	return True

def isComplete(assignment):
	return set(assignment.keys())==set(squares)

def display(values):
	for r in rows:
		if r in 'DG':
			print("------------------------------------------------------------------------------")
		for c in cols:
			if c in '47':
				print (' | ', values[r+c], ' ',end=' ')
			else:
				print(values[r+c], ' ',end=' ')
		print(end='\n')

def write(values):
	solves_sudoku = ""
	for variables in squares:
		solves_sudoku = solves_sudoku + values[variables]
	return solves_sudoku

def Select_Unassigned_Variables(assignment, Sudoku):
	unassigned_Variables = dict((squares, len(Sudoku.values[squares])) for squares in Sudoku.values if squares not in assignment.keys())
	mrv = min(unassigned_Variables, key=unassigned_Variables.get)
	return mrv

# def Select_Unassigned_Variables(assignment, csp):
#     unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
#     mrv = min(unassigned_variables, key=unassigned_variables.get)
#     return mrv

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

