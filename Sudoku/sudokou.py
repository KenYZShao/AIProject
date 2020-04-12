import queue
import time
import sys
from copy import deepcopy
from DFS_Sudoku import solve_dfs
from BFS_Sudoku import solve_bfs
from AC3 import *
from Backtracking import *
import matplotlib.pyplot as plt
import numpy as np

def converttoList(str_grid):
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

def solve_sudoku(inputFile, outputFile):
    # size = dim
    backtrack_execution_times = []
    no_of_boards = []
    array = []  
    with open(inputFile, "r") as lines:
        for line in lines:
            array.append(line)

    lines.close()
    i = 0
    board_no = 0
    start = time.time()
    out = open(outputFile, "w")

    for grid in array:
        # unsolved_String = str(grid)
        # board = converttoList(unsolved_String)
        # startpuzle_dfs = time.time()
        # # solve_dfs(board)
        # total_time = time.time()-startpuzle_dfs
        startpuzle = time.time()
        board_no =  board_no + 1
        no_of_boards.append(board_no)
        # choose_Dimenion(size)
        sudoku = Sudoku(grid=grid)
        # print(sudoku)
        solved = AC3(sudoku)
        if isCompleteAC3(sudoku) and solved:
            end  = time.time()
            execution_time = end - startpuzle
            backtrack_execution_times.append(execution_time)
            print ("The board (solved by AC3 alone) -", board_no, " takes ", time.time() - startpuzle, " seconds")
            print ("After solving: ", write(sudoku.values))
            out.write(write(sudoku.values)+"\n")
            i = i + 1
        else:
            # display(sudoku.values)
            solved  = Backtracking_Search(sudoku)
            if solved!="NOT SOLVED":
                end  = time.time()
                execution_time = end - startpuzle
                backtrack_execution_times.append(execution_time)
                print ("The board-", board_no, " takes ", time.time() - startpuzle, " seconds")
                display(solved)
                out.write(write(solved)+"\n")
                i = i + 1
    out.close()
    
    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)
    return backtrack_execution_times, no_of_boards

def solve_sudoku_bfs(inputFile, outputFile):
    # size = dim
    bfs_execution_times = []
    no_of_boards = []
    array = []  
    with open(inputFile, "r") as lines:
        for line in lines:
            array.append(line)

    lines.close()
    i = 0
    j = 0
    board_no = 0
    start = time.time()
    out = open(outputFile, "w")

    for grid in array:
        unsolved_String = str(grid)
        board = converttoList(unsolved_String)
        startpuzle_bfs = time.time()
        # total_time = time.time()-startpuzle_dfs
        board_no =  board_no + 1
        no_of_boards.append(board_no)

        # solve_dfs(board)
        solved = solve_bfs(board)
        # print("DONE")
        print(solved)
        if (solved == "SOLVED"):
            end  = time.time()
            execution_time = end - startpuzle_bfs
            bfs_execution_times.append(execution_time)
            print ("The board (solved by BFS) -", board_no, " takes ", execution_time, " seconds")
            print ("After solving: ", solved)
            out.write(solved +"\n")
            i = i + 1
        else:
            end  = time.time()
            execution_time = end - startpuzle_bfs
            bfs_execution_times.append(execution_time)
            print ("NO SOLUTION FOUND", board_no)
            j = j + 1

    out.close()
    print ("Number of problems NOT solved is: ", j)
    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)
    return bfs_execution_times, no_of_boards


#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    
    backtrack_execution_time_easy = []
    backtrack_execution_time_hard = []
    backtrack_execution_time_top95 = []
    bfs_execution_time_easy = []
    bfs_execution_time_hard = []
    bfs_execution_time_top95 = []

    dimension = "9"
    if (dimension == "6"):
        from Utilities6x6 import *
    else:
        from Utilities import * 
    
    easy = "/Users/Ayush/Desktop/CS7IS3/easy50_clean.txt"
    hardest = "/Users/Ayush/Desktop/CS7IS3/top95_clean.txt"
    top95 = "/Users/Ayush/Desktop/CS7IS3/hardest_clean.txt"
    solved_easy = "/Users/Ayush/Desktop/CS7IS3/easy_output.txt"
    solved_easy_bfs = "/Users/Ayush/Desktop/CS7IS3/easy_bfs_output.txt"
    solved_hardest = "/Users/Ayush/Desktop/CS7IS3/hardest_output.txt"
    solved_top95 = "/Users/Ayush/Desktop/CS7IS3/top95_output.txt"

    # choose_Dimenion(dimension)
    solve_sudoku(easy,solved_easy)
    backtrack_execution_time_easy,  No_of_boards = solve_sudoku(easy,solved_easy)
    # solve_sudoku(hardest,solved_hardest)
    # solve_sudoku(top95,solved_top95)


    solve_sudoku_bfs(easy,solved_easy_bfs)
    bfs_execution_time_easy, No_of_boards = solve_sudoku_bfs(easy,solved_easy_bfs)
    # execution time plot


    plt.plot(No_of_boards, backtrack_execution_time_easy)
    plt.plot(No_of_boards, bfs_execution_time_easy)
    plt.title("Execution Times")
    plt.xlabel("Number of Boards ")
    plt.ylabel("Time [s]")
    plt.legend(['Backtracking', "BFS"], loc='upper left')
    plt.savefig('execution_times01.png')
    plt.clf()

    # array = []  
    # with open("/Users/Ayush/Documents/GitHub/AI-Sudoku/sudokus_start.txt", "r") as ins:
    #     for line in ins:
    #         array.append(line)

    # ins.close()
    # i = 0
    # boardno = 0
    # start = time.time()
    # f = open("/Users/Ayush/Documents/GitHub/AI-Sudoku/ac3outputtest.txt", "w")

    # for grid in array:
    #     # print(grid)
    #     a_string = str(grid)
    #     board = converttoList(a_string)
    #     # print(board)
    #     startpuzle = time.time()
    #     # solve_dfs(board)
    #     boardno =  boardno + 1
    #     sudoku = csp(grid=grid)
    #     print(sudoku)
    #     solved = AC3(sudoku)
    #     if isCompleteAC3(sudoku) and solved: 
    #         print ("The board (solved by AC3 alone) -", boardno, " takes ", time.time() - startpuzle, " seconds")
    #         print ("After solving: ", write(sudoku.values))
    #         f.write(write(sudoku.values)+"\n")
    #         i = i + 1
    #     else:
    #         display(sudoku.values)
    #         solved  = Backtracking_Search(sudoku)
    #         if solved!="FAILURE":
    #             print ("The board-", boardno, " takes ", time.time() - startpuzle, " seconds")
    #             display(solved)
    #             f.write(write(solved)+"\n")
    #             i = i + 1
    # f.close()

    # print ("Number of problems solved is: ", i)
    # print ("Time taken to solve the puzzles is: ", time.time()-start)