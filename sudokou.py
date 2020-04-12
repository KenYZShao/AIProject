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

        startpuzle = time.time()
        board_no =  board_no + 1
        no_of_boards.append(board_no)
        sudoku = Sudoku(grid=grid)
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
    
    total_backtrack_execution_times = time.time()-start
    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)
    return total_backtrack_execution_times

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
    total_bfs_execution_times = time.time()-start
    print ("Number of problems NOT solved is: ", j)
    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)
    return total_bfs_execution_times

def solve_sudoku_dfs(inputFile, outputFile):
    # size = dim
    dfs_execution_times = []
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
        startpuzle_dfs = time.time()
        # total_time = time.time()-startpuzle_dfs
        board_no =  board_no + 1
        no_of_boards.append(board_no)

        # solve_dfs(board)
        solved = solve_dfs(board)
        # print("DONE")
        print(solved)
        if (solved == "SOLVED"):
            end  = time.time()
            execution_time = end - startpuzle_dfs
            dfs_execution_times.append(execution_time)
            print ("The board (solved by DFS) -", board_no, " takes ", execution_time, " seconds")
            print ("After solving: ", solved)
            out.write(solved +"\n")
            i = i + 1
        else:
            end  = time.time()
            execution_time = end - startpuzle_dfs
            dfs_execution_times.append(execution_time)
            print ("NO SOLUTION FOUND", board_no)
            j = j + 1

    out.close()
    total_dfs_execution_times = time.time()-start
    print ("Number of problems NOT solved is: ", j)
    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)
    return total_dfs_execution_times

#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":
    
    backtrack_execution_time_easy = []
    backtrack_execution_time_hard = []
    backtrack_execution_time_top95 = []
    
    bfs_execution_time_easy = []
    bfs_execution_time_hard = []
    bfs_execution_time_top95 = []

    dfs_execution_time_easy = []
    dfs_execution_time_hard = []
    dfs_execution_time_top95 = []

    dimension = "9"
    if (dimension == "6"):
        from Utilities6x6 import *
    else:
        from Utilities import * 
    
    easy = "/Users/Ayush/Desktop/CS7IS3/easy50_clean.txt"
    solved_easy = "/Users/Ayush/Desktop/CS7IS3/easy_output.txt"
    solved_easy_bfs = "/Users/Ayush/Desktop/CS7IS3/easy_bfs_output.txt"
    solved_easy_dfs = "/Users/Ayush/Desktop/CS7IS3/easy_dfs_output.txt"

    hardest = "/Users/Ayush/Desktop/CS7IS3/hardest_clean.txt"
    solved_hardest_bfs = "/Users/Ayush/Desktop/CS7IS3/hardest_output_bfs.txt"
    solved_hardest_dfs = "/Users/Ayush/Desktop/CS7IS3/hardest_output_dfs.txt"
    solved_hardest = "/Users/Ayush/Desktop/CS7IS3/hardest_output.txt"

    top95 = "/Users/Ayush/Desktop/CS7IS3/top95_clean.txt"
    solved_top95_bfs = "/Users/Ayush/Desktop/CS7IS3/top95_output_bfs.txt"
    solved_top95_dfs = "/Users/Ayush/Desktop/CS7IS3/top95_output_dfs.txt"
    solved_top95 = "/Users/Ayush/Desktop/CS7IS3/top95_output.txt"
 

    # bfs_execution_time_easy = solve_sudoku_bfs(easy,solved_easy_bfs)
    # dfs_execution_time_easy = solve_sudoku_dfs(easy, solved_easy_dfs)
    # backtrack_execution_time_easy = solve_sudoku(easy,solved_easy)

    # Total_Exe_time_easy_50 = []
    # Total_Exe_time_easy_50.append(bfs_execution_time_easy)
    # Total_Exe_time_easy_50.append(dfs_execution_time_easy)
    # Total_Exe_time_easy_50.append(backtrack_execution_time_easy)

    # bfs_execution_time_hard = solve_sudoku_bfs(hardest,solved_hardest_bfs)
    # dfs_execution_time_hard = solve_sudoku_dfs(hardest, solved_hardest_dfs)
    # backtrack_execution_time_hard = solve_sudoku(hardest,solved_hardest)
    

    # Total_Exe_time_hard = []
    # Total_Exe_time_hard.append(bfs_execution_time_hard)
    # Total_Exe_time_hard.append(dfs_execution_time_hard)
    # Total_Exe_time_hard.append(backtrack_execution_time_hard)

    backtrack_execution_time_top95 =  solve_sudoku(top95,solved_top95)
    dfs_execution_time_top95 =   solve_sudoku_dfs(top95, solved_top95_dfs)
    bfs_execution_time_top95 =  solve_sudoku_bfs(top95,solved_top95_bfs)
    

    Total_Exe_time_top95 = []
    Total_Exe_time_top95.append(bfs_execution_time_top95)
    Total_Exe_time_top95.append(dfs_execution_time_top95)
    Total_Exe_time_top95.append(backtrack_execution_time_top95)

    # x_axis = ["BFS", "DFS", "Backtrack" ]
    # x_pos = [i for i, _ in enumerate(x_axis)]
    # plt.bar(x_axis, Total_Exe_time_easy_50)
    # plt.title("Execution Times for Easy50")
    # plt.xlabel("Algorithms")
    # plt.ylabel("Time [s]")
    # plt.minorticks_on()
    # # plt.legend(["BFS","DFS","Backtracking"], loc='upper left')
    # for i, v in enumerate(Total_Exe_time_easy_50):
    #     plt.text(x_pos[i] - 0.41, v + 0.51, str(v))
    # plt.savefig('2execution_timesEASY50.png')
    # plt.clf()


    # x_axis = ["BFS", "DFS", "Backtrack" ]
    # x_pos = [i for i, _ in enumerate(x_axis)]
    # plt.bar(x_axis, Total_Exe_time_top95)
    # plt.title("Execution Times for Easy50")
    # plt.xlabel("Algorithms")
    # plt.ylabel("Time [s]")
    # plt.minorticks_on()
    # # plt.legend(["BFS","DFS","Backtracking"], loc='upper left')
    # for i, v in enumerate(Total_Exe_time_hard):
    #     plt.text(x_pos[i] - 0.41, v + 0.51, str(v))
    # plt.savefig('execution_times_hardest.png')
    # plt.clf()

    x_axis = ["BFS", "DFS", "Backtrack" ]
    x_pos = [i for i, _ in enumerate(x_axis)]
    plt.bar(x_axis, Total_Exe_time_top95)
    plt.title("Execution Times for Top95")
    plt.xlabel("Algorithms")
    plt.ylabel("Time [s]")
    plt.minorticks_on()
    # plt.legend(["BFS","DFS","Backtracking"], loc='upper left')
    for i, v in enumerate(Total_Exe_time_top95):
        plt.text(x_pos[i] - 0.41, v + 0.51, str(v))
    plt.savefig('execution_times_hardest.png')
    plt.clf()


    # Total_Exe_time_easy_50 = [997.0055570602417, 330.22495579719543, 11.127339124679565]