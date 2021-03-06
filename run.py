import random
import numpy as np


# Prints the array in format so it is readable(a bit at least)

def show_board(board):
    for i in range(9):# i represents row
        for j in range(9):# j represents column
            if  j == 0:
                print("|", end='')
            if  j != 8:
                print(board[i, j], end=' ')
            else:
                print(board[i, j], end='')
            if (j+1) % 3 == 0:
                print("|", end='')
        if (i+1) % 3 == 0:
            print("\n---------------------", end='')
        print()

# This function finds an empty cell

def find_next_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i, j] == 0:
                row = i
                col = j
                fill_check = 1
                res = np.array([row, col, fill_check], dtype="int8")
                return res
    res = np.array([-1, -1, 0])
    return res

# This function checks the validity of a number at a given position in the puzzle
# Done according to sudoku rules

def check_input_validity(board, row, col, num):
    row_start = (row//3) * 3
    col_start = (col//3) * 3
    if num in board[:, col] or num in board[row, :]:
        return False
    if num in board[row_start:row_start + 3, col_start:col_start + 3]:
        return False
    return True

# Generates an unsolved sudoku board based on required difficulty
# The algorithm for difficulty generation is helpful for accuracy

def unsolved_puzzle(board, difficulty):
    count, done = 0, False
    if difficulty == "Easy":
        print("Play SmashSudoku easy puzzle...\n\n")
        upper_limit = 35
    elif difficulty == "Medium":
        print("Play SmashSudoku medium puzzle ...\n\n")
        upper_limit = 41
    else:
        print("Play SmashSudoku fiendishly difficult puzzle ...\n\n")
        upper_limit = 47
    while True:
        i = random.randint(0, 8)
        j = random.randint(0, 8)
        if count <= upper_limit:
            if board[i, j] != 0:
                not_check = board[i, j]
                board[i, j] = 0
                board_copy = board
                if solve_sudoku(board_copy, not_check):
                    board[i, j] = not_check
                    continue
                row_start = (i//3) * 3
                col_start = (j//3) * 3
                if difficulty == "Easy":
                    if np.count_nzero(board[row_start:row_start + 3, col_start:col_start + 3]) < 5:
                        board[i, j] = not_check
                        continue
                elif difficulty == "Medium":
                    if np.count_nzero(board[row_start:row_start + 3, col_start:col_start + 3]) < 4:
                        board[i, j] = not_check
                        continue
                else:
                    if np.count_nzero(board[row_start: row_start + 3, col_start:col_start + 3]) < 3:
                        board[i, j] = not_check
                count += 1
        else:
            done = True
            break

# Input of the row, column and nummber to check is done here

def play_game(solved_board, unsolved_board):
    while True:
        row = int(input("Enter row number (1-9):\n")) - 1
        col = int(input("Enter column number (1-9):\n")) - 1
        number_check = int(input("Enter the number((1-9) or input 10 to exit):\n"))
        if number_check != 10:
            if unsolved_board[row, col] == 0:
                print(solved_board[row, col])
                if solved_board[row, col] == number_check:
                    print("Correct! Board Updated:")
                    unsolved_board[row, col]= number_check
                    show_board(unsolved_board)
                else:
                    print("Incorrect! Try again!:")
                    show_board(unsolved_board)
            else:
                print("Location is already filled!")
            if np.array_equal(solved_board, unsolved_board):
                print("Congrats on solving the sudoku!")
                break
        else:
            print("\nThe solved board is:")
            show_board(solved_board)
            print("\nThank you for playing!\nWe hope to see you again.")# done
            return

# Solving any unsolved sudoku puzzle is done here, first call generates a solved puzzle
# Uses a backtracking algorithm

def solve_sudoku(board, not_check):
    guess = find_next_empty(board)
    if guess[2] == 0:
        return True
    else:
        row = guess[0]
        col = guess[1]
        for i in np.random.permutation(10):
            if i != 0 and i != not_check:
                if check_input_validity(board, row, col, i):
                    board[row, col] = i
                    if solve_sudoku(board, not_check):
                        return True
                    board[row, col] = 0
    return False


# Inputs difficulty and initializes playing board

def main():
    user_choice = int(input("Welcome! Choose level-\n1.Easy\n2.Medium\n3.Hard\nYour choice:"))#done
    if user_choice == 1:
        difficulty = "Easy"
    elif user_choice == 2:
        difficulty = "Medium"
    else:
        difficulty = "Hard"
    board = np.zeros((9, 9), dtype="int8")
    if solve_sudoku(board, -1):
        solved_board = board.copy()
        print("\n\nThe unsolved puzzle is:\n")
        unsolved_puzzle(board, difficulty)
        show_board(board)
        unsolved_board = board.copy()
        play_game(solved_board, unsolved_board)
    else:
        print("There is no solution!")
    return

if __name__ == "__main__":
    main()