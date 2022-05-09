import numpy as np 
import random 

#Prints the ndarray in format so it is readable(a bit at least)

def Show_Board(board):
    for i in range(9): #i represents row 
        for j in range(9): #j represents columns 
            if j==0:
                print("|",end='')
            if j!=8:
                print(board[i,j],end=' ')
            else:
                print(board[i,j],end='')
            if (j+1)%3==0:
                print("|",end='')
        if (i+1)%3==0:
            print("\n---------------------",end='')
        print()

#This function finds an empty cell

def find_next_empty(board):
    for i in range(9):
        for j in range(9): 
            if board[i,j]==0: 
                row=i 
                col=j 
                Fill_Chk=1 
                res=np.array([row,col,Fill_Chk],dtype="int8")
                return res  
    res=np.array([-1,-1,0])
    return res 

#This function checks the validity of a number at a given position in the puzzle 
#Done according to sudoku rules 

def check_input_validity(board,row,col,num):
    row_start=(row//3)*3 
    col_start=(col//3)*3 
    if num in board[:,col] or num in board[row,:]: 
        return False 
    if num in board[row_start:row_start+3,col_start:col_start+3]: 
        return False
    return True 

#Generates an unsolved sudoku board based on required difficulty
#The algorithm for difficulty generation is a little primitive, but really helpful for accuracy 

def unsolved_puzzle(board,difficulty): 
    count,done=0,False 
    if difficulty == "Easy": 
        print("Generating Easy Difficulty Puzzle...\n\n")
        upper_limit=35
    elif difficulty == "Medium": 
        print("Generating Medium Difficulty Puzzle ...\n\n")
        upper_limit=41
    else: 
        print("Generating Hard Difficulty Puzzle ...\n\n")
        upper_limit=47
    while True:  
        i=random.randint(0,8) 
        j=random.randint(0,8) 
        if count<=upper_limit: 
            if board[i,j]!=0: 
                not_check=board[i,j]
                board[i,j]=0
                board_copy=board
                if solve_sudoku(board_copy,not_check):
                    board[i,j]=not_check 
				    continue 
                row_start=(i//3)*3 
                col_start=(j//3)*3 
                if difficulty == "Easy": 
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<5: 
                        board[i,j]=not_check
                        continue 
                elif difficulty == "Medium": 
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<4: 
                        board[i,j]=not_check 
                        continue 
                else:
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<3: 
                        board[i,j]=not_check 
                count+=1
        else:
            done=True
            break

#Input of the row, column and nummber to check is done here, so essentially playing the game lol

def play_game(solved_board, unsolved_board): 
    while True:    
        row=int(input("Enter row number (1-9):\n")) - 1 
        col=int(input("Enter column number (1-9):\n")) - 1 
        number_check=int(input("Enter the number((1-9) or input 10 to exit):\n"))
        if number_check!=10: 
            if unsolved_board[row,col]==0:
                print(solved_board[row,col])
                if solved_board[row,col]==number_check: 
                    print("Correct! Board Updated:") 
                    unsolved_board[row,col]=number_check
                    Show_Board(unsolved_board)
                else:
                    print("Incorrect! Board Updated:")
                    Show_Board(unsolved_board)
            else:
                print("Location is already filled!")
            if np.array_equal(solved_board,unsolved_board):
                print("Congrats on solving the sudoku!")
                break
        else:
            print("\nThe solved board is:")
            Show_Board(solved_board)
            print("\nThank you for playing!\nWe hope to see you again.")#done
            return 

#Solving any unsolved sudoku puzzle is done here, first call generates a solved puzzle
#Uses a backtracking algorithm 

def solve_sudoku(board,not_check):
    x=find_next_empty(board)
    if x[2]==0:
        return True 
    else: 
        row=x[0]
        col=x[1]
        for i in np.random.permutation(10): 
            if i!=0 and i!=not_check: 
                if check_input_validity(board,row,col,i):
                    board[row,col]=i 
                    if solve_sudoku(board,not_check): 
                        return True 
                    board[row,col]=0 
    return False 

#Inputs difficulty and initializes playing board

def main():
    ch=int(input("Hello!Choose the level of difficulty-\n1.Easy\n2.Medium\n3.Hard\nYour choice:"))#done
    if ch==1:
        difficulty="Easy"
    elif ch==2:
        difficulty="Medium" 
    else:
        difficulty="Hard"
    board=np.zeros((9,9),dtype="int8")
    if solve_sudoku(board,-1):
        solved_board=board.copy()
        print("\n\nThe unsolved puzzle is:\n")
        unsolved_puzzle(board,difficulty)
        Show_Board(board)
        unsolved_board=board.copy()
        play_game(solved_board, unsolved_board)
    else:
        print("The board is not possible!")
    return

if __name__=="__main__":
    main()