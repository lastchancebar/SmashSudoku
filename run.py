import numpy as np #done
import random #done

#Prints the ndarray in format so it is readable(a bit at least)

def Show_Board(board):#done
    for i in range(9): #i represents row #done
        for j in range(9): #j represents columns #done
            if j==0:#done
                print("|",end='')#done
            if j!=8:
                print(board[i,j],end=' ')#done
            else:
                print(board[i,j],end='')#done
            if (j+1)%3==0:#done
                print("|",end='')#done
        if (i+1)%3==0:
            print("\n---------------------",end='')# done
        print()#done

#This function finds...well...an empty cell

def find_next_empty(board):#dione
    for i in range(9):#done
        for j in range(9): #done
            if board[i,j]==0: #done
                row=i #done
                col=j #done
                Fill_Chk=1 #done
                res=np.array([row,col,Fill_Chk],dtype="int8")#done res=result
                return res  # done
    res=np.array([-1,-1,0])#done
    return res #done

#This function checks the validity of a number at a given position in the puzzle 
#Done according to sudoku rules #done

def check_input_validity(board,row,col,num):#done
    row_start=(row//3)*3 #done
    col_start=(col//3)*3 #done
    if num in board[:,col] or num in board[row,:]: #done
        return False #done
    if num in board[row_start:row_start+3,col_start:col_start+3]: #done
        return False #done
    return True #done

#Generates an unsolved sudoku board based on required difficulty
#The algorithm for difficulty generation is a little primitive, but really helpful for accuracy 

def unsolved_puzzle(board,difficulty): # done
    count,done=0,False #done
    if difficulty == "Easy": #done
        print("Generating Easy Difficulty Puzzle...\n\n")#done
        upper_limit=35#done
    elif difficulty == "Medium": #done
        print("Generating Medium Difficulty Puzzle ...\n\n")#done
        upper_limit=41#done
    else: #done
        print("Generating Hard Difficulty Puzzle ...\n\n")#done
        upper_limit=47#done
    while True:  #done 
        i=random.randint(0,8) #done
        j=random.randint(0,8) #done
        if count<=upper_limit: #done
            if board[i,j]!=0: #done
                not_check=board[i,j]#done
                board[i,j]=0#done
                board_copy=board#done
                if solve_sudoku(board_copy,not_check):#done
                    board[i,j]=not_check #done
					continue #done
                row_start=(i//3)*3 #done
                col_start=(j//3)*3 #done
                if difficulty == "Easy": #done
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<5: #done
                        board[i,j]=not_check#done
                        continue #done
                elif difficulty == "Medium": #done
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<4: #done
                        board[i,j]=not_check #done
                        continue #done
                else: #done
                    if np.count_nonzero(board[row_start:row_start+3,col_start:col_start+3])<3: #done
                        board[i,j]=not_check #done
                count+=1#done
        else:#done
            done=True#done
            break#done

#Input of the row, column and nummber to check is done here, so essentially playing the game lol

def play_game(solved_board, unsolved_board): #done
    while True:  #done  
        row=int(input("Enter row number (1-9):")) - 1 #done
        col=int(input("Enter column number (1-9):")) - 1 #done
        number_check=int(input("Enter the number((1-9) or input 10 to exit):"))#done
        if number_check!=10: #done
            if unsolved_board[row,col]==0:#done
                print(solved_board[row,col])#done
                if solved_board[row,col]==number_check: #done
                    print("Correct! Board Updated:") #done
                    unsolved_board[row,col]=number_check#done
                    Show_Board(unsolved_board)#done
                else:#done
                    print("Incorrect! Board Updated:")#done
                    Show_Board(unsolved_board)#done
            else:
                print("Location is already filled!")#done
            if np.array_equal(solved_board,unsolved_board):#done
                print("Congrats on solving the sudoku!")#done
                break#done
        else:#done
            print("\nThe solved board is:")#done
            Show_Board(solved_board)#done
            print("\nThank you for playing!\nWe hope to see you again.")#done
            return #done

#Solving any unsolved sudoku puzzle is done here, first call generates a solved puzzle
#Uses a backtracking algorithm 

def solve_sudoku(board,not_check):#done
    x=find_next_empty(board)#done
    if x[2]==0:#done
        return True #done
    else: #done
        row=x[0]#done
        col=x[1]#done
        for i in np.random.permutation(10): #done
            if i!=0 and i!=not_check: #done
                if check_input_validity(board,row,col,i):#done
                    board[row,col]=i #done
                    if solve_sudoku(board,not_check): #done
                        return True #done
                    board[row,col]=0 #done 
    return False #done

#Inputs difficulty and initializes playing board

def main():#done
    ch=int(input("Hello!Choose the level of difficulty-\n1.Easy\n2.Medium\n3.Hard\nYour choice:"))#done
    if ch==1:#done
        difficulty="Easy"#done
    elif ch==2:#done
        difficulty="Medium" #done
    else:#done
        difficulty="Hard"#done
    board=np.zeros((9,9),dtype="int8")#done
    if solve_sudoku(board,-1):#done
        solved_board=board.copy()#done
        print("\n\nThe unsolved puzzle is:\n")#done
        unsolved_puzzle(board,difficulty)
        Show_Board(board)
        unsolved_board=board.copy()
        play_game(solved_board, unsolved_board)
    else:
        print("The board is not possible!")
    return

if __name__=="__main__":
    main()