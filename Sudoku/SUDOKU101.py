# THE WRAPPER FUNCTION WHICH SOLVES ALL THE SUDOKU PROBLEMS IN THE INPUT FILE USING BACKTRACKING AND WRITES THE OUTPUT TO THE OUTPUT FILE 

import sys #For getting the values from command line 
from DRIVER101 import *
from DFS_Sudoku import solve_dfs
import time 

def converttolist(str_grid):
    # print(str_grid)
    split_strings = []
    n  = 9
    for index in range(0, len(str_grid), n):
        split_strings.append(str_grid[index : index + n])

    # print(split_strings)
    split_strings.pop()
    listoflist = []
    result = []
    # new_list2 = list(split_strings[0])
    for i in split_strings:
        listoflist.append(list(i))

    result = [[int(float(j)) for j in i] for i in listoflist]
    return result

#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    '''
    The function takes arguments from commandline
    Argument 1 - Python file name 
    Argument 2 - Input String Showing the Sudoku 
    '''
    array = []  
    with open("/Users/Ayush/Documents/GitHub/AI-Sudoku/sudokus_start.txt", "r") as ins:
        for line in ins:
            array.append(line)

    ins.close()
    i = 0
    boardno = 0
    start = time.time()
    f = open("/Users/Ayush/Documents/GitHub/AI-Sudoku/ac3outputtest.txt", "w")

    for grid in array:
        # print(grid)
        a_string = str(grid)
        board = converttolist(a_string)
        # print(board)
        startpuzle = time.time()
        # solve_dfs(board)
        boardno =  boardno + 1
        sudoku = csp(grid=grid)
        print(sudoku)
        solved = AC3(sudoku)
        if isCompleteAC3(sudoku) and solved: 
            print ("The board (solved by AC3 alone) -", boardno, " takes ", time.time() - startpuzle, " seconds")
            print ("After solving: ", write(sudoku.values))
            f.write(write(sudoku.values)+"\n")
            i = i + 1
        else:
            display(sudoku.values)
            solved  = Backtracking_Search(sudoku)
            if solved!="FAILURE":
                print ("The board-", boardno, " takes ", time.time() - startpuzle, " seconds")
                display(solved)
                f.write(write(solved)+"\n")
                i = i + 1
    f.close()

    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)