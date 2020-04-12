import time
import sys


def converttoList(str_grid, size):
    # print(str_grid)
    split_strings = []
    n  = size
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

def solve_easy(inputFile, outputFile):
    # dimension = "9"
    # if (dimension == "6"):
    #     from NEWDRIVER import *
    # else:
    #     from NEWDRIVER6x6 import *
    # size = dim
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
        # choose_Dimenion(size)
        sudoku = Sudoku(grid=grid)
        # print(sudoku)
        solved = AC3(sudoku)
        if isCompleteAC3(sudoku) and solved: 
            print ("The board (solved by AC3 alone) -", board_no, " takes ", time.time() - startpuzle, " seconds")
            print ("After solving: ", write(sudoku.values))
            out.write(write(sudoku.values)+"\n")
            i = i + 1
        else:
            display(sudoku.values)
            solved  = Backtracking_Search(sudoku)
            if solved!="NOT SOLVED":
                print ("The board-", board_no, " takes ", time.time() - startpuzle, " seconds")
                display(solved)
                out.write(write(solved)+"\n")
                i = i + 1
    out.close()

    print ("Number of problems solved is: ", i)
    print ("Time taken to solve the puzzles is: ", time.time()-start)


#THE MAIN FUNCTION GOES HERE
if __name__ == "__main__":

    dimension = "9"
    if (dimension == "6"):
        from NEWDRIVER6x6 import *
    else:
        from NEWDRIVER import *
    
    easy = "/Users/Ayush/Desktop/CS7IS3/easy50_clean.txt"
    hardest = "/Users/Ayush/Desktop/CS7IS3/top95_clean.txt"
    top95 = "/Users/Ayush/Desktop/CS7IS3/hardest_clean.txt"
    dimension = "9"
    solved_easy = "/Users/Ayush/Desktop/CS7IS3/easy_output.txt"
    solved_hardest = "/Users/Ayush/Desktop/CS7IS3/hardest_output.txt"
    solved_top95 = "/Users/Ayush/Desktop/CS7IS3/top95_output.txt"
    # choose_Dimenion(dimension)
    solve_easy(easy,solved_easy)
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