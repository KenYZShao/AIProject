# INCLUDES THE HELPER FUNCTIONS AND VARIABLES USED BY THE PROGRAM

import queue
import time
from copy import deepcopy

digits =  cols = "123456789"
rows = "ABCDEFGHI"


#FINDING THE CROSS PRODUCT OF TWO SETS 
def cross(A, B):
    return [a + b for a in A for b in B]

squares = cross(rows, cols)


# CLASS DESCRIPTION FOR CSP
class csp:
    
    #INITIALIZING THE CSP
    def __init__ (self, domain = digits, grid = ""):
        self.variables = squares
        self.domain = self.getDict(grid)
        self.values = self.getDict(grid)        

        '''
            Unitlist consists of the 27 lists of peers 
            Units is a dictionary consisting of the keys and the corresponding lists of peers 
            Peers is a dictionary consisting of the 81 keys and the corresponding set of 20 peers 
            Constraints denote the various all-different constraints between the variables 
        '''

        self.unitlist = ([cross(rows, c) for c in cols] +
                         [cross(r, cols) for r in rows] +
                         [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in squares)
        self.peers = dict((s, set(sum(self.units[s],[]))-set([s])) for s in squares)
        self.constraints = {(variable, peer) for variable in self.variables for peer in self.peers[variable]}




    #GETTING THE STRING AS INPUT AND RETURNING THE CORRESPONDING DICTIONARY
    def getDict(self, grid=""):
        i = 0
        values = dict()
        for cell in self.variables:
            if grid[i]!='0':
                values[cell] = grid[i]
            else:
                values[cell] = digits
            i = i + 1
        return values


# IMPLEMENTATION OF AC3 ALGORITHM

#THE MAIN AC-3 ALGORITHM
def AC3(csp):
    q = queue.Queue()

    for arc in csp.constraints:
        q.put(arc)

    i = 0
    while not q.empty():
        (Xi, Xj) = q.get()

        i = i + 1 

        if ReviseAC3(csp, Xi, Xj):
            if len(csp.values[Xi]) == 0:
                return False

            for Xk in (csp.peers[Xi] - set(Xj)):
                q.put((Xk, Xi))

    #display(csp.values)
    return True 


#WORKING OF THE REVISE ALGORITHM
def ReviseAC3(csp, Xi, Xj):
    revised = False
    values = set(csp.values[Xi])

    for x in values:
        if not isconsistentAC3(csp, x, Xi, Xj):
            csp.values[Xi] = csp.values[Xi].replace(x, '')
            revised = True 

    return revised 



#CHECKS IF THE GIVEN ASSIGNMENT IS CONSISTENT
def isconsistentAC3(csp, x, Xi, Xj):
    for y in csp.values[Xj]:
        if Xj in csp.peers[Xi] and y!=x:
            return True

    return False


#DISPLAYS THE SUDOKU IN THE GRID FORMAT
def display(values):
    for r in rows:
        if r in 'DG':
            print ("------------------------------------------------------------------------------")
        for c in cols:
            if c in '47':
                print (' | ', values[r+c], ' ',end=' ')
            else:
                print (values[r+c], ' ',end=' ')
        print (end='\n')

        

#CHECKS IF THE SUDOKU IS COMPLETE OR NOT
def isCompleteAC3(csp):
    for variable in squares:
        if len(csp.values[variable])>1:
            return False
    return True


#WRITES THE SOLVED SUDOKU IN THE FORM OF A STRING
def write(values):
    output = ""
    for variable in squares:
        output = output + values[variable]
    return output

#BACKTRACKING SEARCH INITIALIZES THE INITIAL ASSIGNMENT AND CALLS THE BACKTRACK FUNCTION
def Backtracking_Search(csp):
    return Backtrack({}, csp)



#THE RECURSIVE FUNCTION WHICH ASSIGNS VALUE USING BACKTRACKING 
def Backtrack(assignment, csp):

    if isComplete(assignment):
        return assignment

    var = Select_Unassigned_Variables(assignment, csp)
    domain = deepcopy(csp.values)

    for value in csp.values[var]:
        if isConsistent(var, value, assignment, csp):
            assignment[var] = value
            inferences = {}
            inferences = Inference(assignment, inferences, csp, var, value)
            if inferences!= "FAILURE":
                result = Backtrack(assignment, csp)
                if result!="FAILURE":
                    return result

            del assignment[var]
            csp.values.update(domain)

    return "FAILURE"

# function recursiveBacktrackingSearch(assignment, csp):
#   if assignment.isComplete():
#     return assignment
    
#   variable = selectUnassignedVariable(csp.variables())
#   for each value in orderDomainValues(csp.domain()):
#     if assignment.isConsistentWith(csp.constraints()):
#       assignment.add(variable, value)
#       result = recursiveBacktrackingSearch(assignment, csp)
#       if result is false:
#         return result
#       assignment.remove(variable, value);
#   return false



#FORWARD CHECKING USING THE CONCEPT OF INFERENCES
def Inference(assignment, inferences, csp, var, value):
    inferences[var] = value

    for neighbor in csp.peers[var]:
        if neighbor not in assignment and value in csp.values[neighbor]:
            if len(csp.values[neighbor])==1:
                return "FAILURE"

            remaining = csp.values[neighbor] = csp.values[neighbor].replace(value, "")

            if len(remaining)==1:
                flag = Inference(assignment, inferences, csp, neighbor, remaining)
                if flag=="FAILURE":
                    return "FAILURE"

    return inferences

            
#CHECKS IF THE ASSIGNMENT IS COMPLETE
def isComplete(assignment):
    return set(assignment.keys())==set(squares)



#SELECTS THE NEXT VARIABLE TO BE ASSIGNED USING MRV
def Select_Unassigned_Variables(assignment, csp):
    unassigned_variables = dict((squares, len(csp.values[squares])) for squares in csp.values if squares not in assignment.keys())
    mrv = min(unassigned_variables, key=unassigned_variables.get)
    return mrv



#RETURNS THE STRING OF VALUES OF THE GIVEN VARIABLE 
# def Order_Domain_Values(var, assignment, csp):
#   return csp.values[var]

# Most Constrained Variable heuristic
# Pick the unassigned variable that has fewest legal values remaining.

# def select_unassigned_variable(assignment, sudoku):
#     unassigned_variables = [v for v in sudoku.variables if v not in assignment]
#     mcv = min(unassigned_variables, key=lambda var: len(sudoku.domains[var]))
#     return mcv


#CHECKS IF THE GIVEN NEW ASSIGNMENT IS CONSISTENT
def isConsistent(var, value, assignment, csp):
    for neighbor in csp.peers[var]:
        if neighbor in assignment.keys() and assignment[neighbor]==value:
            return False
    return True



#PERFORMS FORWARD-CHECKING
# def forward_check(csp, assignment, var, value):
#   csp.values[var] = value
#   for neighbor in csp.peers[var]:
#       csp.values[neighbor] = csp.values[neighbor].replace(value, '')


