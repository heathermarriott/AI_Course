import copy
COL=3
ROW=3
board=[[0,1,2],[3,4,5],[6,7,8]] 

def check_winner(current_board): #-1=Xs 0=tie, 1=Os O maximizing player,X min
    for row in range(ROW):  #check all rows
        if current_board[row][0]==current_board[row][1]==current_board[row][2]:
            return -1 if current_board[row][0]=='X' else 1
    for col in range(COL):  #check all columns
        if current_board[0][col]==current_board[1][col]==current_board[2][col]:
            return -1 if current_board[0][col]=='X' else 1
    #check the diagonals
    if current_board[0][0]==current_board[1][1]==current_board[2][2]:
            return -1 if current_board[0][0]=='X' else 1
    if current_board[2][0]==current_board[1][1]==current_board[0][2]:
            return -1 if current_board[2][0]=='X' else 1
    return 0

def legal_move(current_board, move):
    if current_board[move//3][move%3]=='X' or current_board[move//3][move%3]=='O':
        return False
    return True

def print_board(current_board):
    for row in range(ROW):
        for col in range(COL):
            print(f' {current_board[row][col]}  ', end='')
            
            if col < COL-1:
                print('|', end='')
        if row < ROW-1:
            print('\n', '-'*12)
    print('\n')

def ai_move(current_board):
    max_score=-2
    make_move=-1
    #look at all possible moves and select max
    for move in range(9):
        if legal_move(current_board, move):
            #deep copy of board
            copy_board=copy.deepcopy(board)
            copy_board[move//3][move%3]='O'
            score=check_winner(copy_board)
            
            if score > max_score:
                max_score=score
                make_move=move
            
    return [make_move, max_score]

print_board(board)
num_moves=0
marker='X'
while num_moves < 9 and (check_winner(board)==0):
    print('\n\n')
    if marker=='X':
        move=int(input(f"{marker} Enter your move:"))
    else:
        [move,temp] = ai_move(board)
    while not legal_move(board, move):
        print("Illegal move")
        move=int(input("\n\nEnter your move:"))
    board[move//3][move%3] = marker
    
    if marker=='X':
        marker='O'
    else:
        marker='X'
    num_moves+=1
    print_board(board)

w=check_winner(board)
    
if w==0:
    print('Tie')
elif w==-1:
    print('X wins')
else:
    print('O wins')

print_board(board)
num_moves=0
marker='X'

while num_moves < 9 and (check_winner(board)==0):
    print('\n\n')
    if marker=='X':
        move=int(input(f"{marker} Enter your move:"))
    else:
        [move,temp] = ai_move(board)

    while not legal_move(board, move):
        print("Illegal move")
        move=int(input("\n\nEnter your move:"))
    board[move//3][move%3] = marker

    if marker=='X':
        marker='O'
    else:
        marker='X'
    num_moves+=1
    print_board(board)


w=check_winner(board)
    
if w==0:
    print('Tie')
elif w==-1:
    print('X wins')
else:
    print('O wins')

