from Utilities import *
import queue
import time
from copy import deepcopy

def isconsistentAC3(Sudoku, x, Xi, Xj):
	for y in Sudoku.values[Xj]:
		if Xj in Sudoku.peers[Xi] and y!=x:
			return True
	return False

def isCompleteAC3(Sudoku):
	for variables in squares:
		if len(Sudoku.values[variables])>1:
			return False
	return True

def ReviseAC3(Sudoku, Xi, Xj):
	isRevised = False
	values = set(Sudoku.values[Xi])

	for x in values:
		if not isconsistentAC3(Sudoku, x, Xi, Xj):
			Sudoku.values[Xi] = Sudoku.values[Xi].replace(x, '')
			isRevised = True
			
	return isRevised

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

def write(values):
	solves_sudoku = ""
	for variables in squares:
		solves_sudoku = solves_sudoku + values[variables]
	return solves_sudoku

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

