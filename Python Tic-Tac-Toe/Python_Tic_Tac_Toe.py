#Author: M3saR
#Release date: 19.07.2023

from random import randrange, randint

board=[[1,2,3],[4,5,6],[7,8,9]]
ending=False
def display_board(board):
    print("+-------+-------+-------+ \n\
|       |       |       |   \n\
|   ",board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],"   |   \n\
|       |       |       |   \n\
+-------+-------+-------+   \n\
|       |       |       |   \n\
|   ",board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |   \n\
|       |       |       |   \n\
+-------+-------+-------+   \n\
|       |       |       |   \n\
|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |   \n\
|       |       |       |   \n\
+-------+-------+-------+", sep='')

def who_first():
    first=input("Who first?\n1 - You\n2 - Computer \nElse - Random\n")
    if first=='1':
        return True
    elif first=='2':
        return False
    else:
        first=randint(1,2)
        if first==1:
            print("Your move: ")
            return True
        else:
            print("Computer move: ")
            return False

def player_move(board):
    try:
        square=int(input("Choose a number: "))
    except:
        print("You must choose a number. Try again in new game")
        return True
    while 1==1:
        
        while square<1 or square>9:
            try:
                square=int(input("Choose correct number: "))
            except:
                print("You must choose a number. Try again in new game")
                return True
        if square == 1 or square == 2 or square == 3:
            x=0
        elif square == 4 or square == 5 or square == 6:
            x=1
        else:
            x=2

        if square == 1 or square == 4 or square == 7:
            y=0
        elif square == 2 or square == 5 or square == 8:
            y=1
        elif square == 3 or square == 6 or square == 9:
            y=2   
        if board[x][y]==square:
            board[x][y]='O'
            break
        else:
            try:
                square=int(input(("This square is taken. Please try again ")))
            except:
                print("You must choose a number. Try again in new game")
                return True

def free_fields(board):
    free_square=[]
    for x in range(3):
        for y in range(3):
            if board[x][y]!='O' and board[x][y]!='X':
                free=(x,y)
                free_square.append(free)
    return free_square

def victory(board, sign):
    if board[0][0]==board[0][1]==board[0][2] or board[1][0]==board[1][1]==board[1][2] or board[2][0]==board[2][1]==board[2][2] or \
        board[0][0]==board[1][0]==board[2][0] or board[0][1]==board[1][1]==board[2][1] or board[0][2]==board[1][2]==board[2][2] or \
        board[0][0]==board[1][1]==board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        if sign==True:
            print("You won")
        else:
            print("Computer move:")
            display_board(board)
            print("You lost")
        return True

def computer_move(board):
    computer_square=False
    while computer_square==False:
        x=randrange(3)
        y=randrange(3)
        if board[x][y]!='O' and board[x][y]!='X':
            board[x][y]='X'
            computer_square=True

sign=who_first()

while ending==False:
    if sign==False:
        computer_move(board)
    display_board(board)
    if player_move(board)==True:
        break
    print('Your move:')
    display_board(board)
    if victory(board, sign)==True:
        break
    sign=False
    computer_move(board)
    if victory(board, sign) ==True:
        break
    sign=True
    if free_fields(board)==[]:
        print("Draw")
        display_board(board)
        break
    print("Computer move")
