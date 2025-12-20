import heapq
import time

#begin_puzzle=[[2,5,3],[1,9,6],[4,7,8]]
#begin_puzzle=[[8,5,1],[7,9,4],[6,3,2]]
#begin_puzzle=[[8,1,6],[2,9,4],[7,3,5]]
begin_puzzle=[[8,10,12,11],[9,16,3,15],[1,7,14,2],[4,13,5,6]] #16 is blank
begin_puzzle=[[12,15,14,4],[3,8,1,9],[6,10,11,2],[5,7,13,16]] #16 is blank
#begin_puzzle=[[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,16,15]]
def print_board(board):
    letterLength = len(str(len(board)**2))
    print("-"*(len(board)*4+letterLength))
    for r in board:
        for x in r:
            if x!= len(board)**2:
                print(f"| {' '*(letterLength-len(str(x)))}{x} |",end='')
            else:
                print(f"| {' '*letterLength} |",end='')
        print("")
        print("-"*(len(board)*4+letterLength))

#take current board, return all possible other boards
#when legal move taken
def deep_copy(board):
    #makes a deep copy of board
    new_array=[[j for j in i ] for i in board]
    #print(new_array)
    return new_array

def next_moves(board):
    nine_row=0
    nine_col=0
    #figure out where blank space is (9 pos)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]== len(board)**2:
                nine_row=i
                nine_col=j
    pos=[] #possible next boards
    if nine_row>0: #could swap up
        up_board=deep_copy(board)
        up_board[nine_row -1][nine_col]=board[nine_row][nine_col]
        up_board[nine_row][nine_col]=board[nine_row-1][nine_col]
        pos.append(up_board)
    if nine_row< len(board)-1: #could swap down
        down_board=deep_copy(board)
        down_board[nine_row +1][nine_col]=board[nine_row][nine_col]
        down_board[nine_row][nine_col]=board[nine_row+1][nine_col]
        pos.append(down_board)
    if nine_col>0: #could swap left
        left_board=deep_copy(board)
        left_board[nine_row][nine_col-1]=board[nine_row][nine_col]
        left_board[nine_row][nine_col]=board[nine_row][nine_col-1]
        pos.append(left_board)
    if nine_col<len(board)-1: #could swap right
        right_board=deep_copy(board)
        right_board[nine_row][nine_col+1]=board[nine_row][nine_col]
        right_board[nine_row][nine_col]=board[nine_row][nine_col+1]
        pos.append(right_board)
    return pos

def Dijkstras(start_node):
    #will use a priority queue instead of queue
    startTime = time.time()
    heap = []
    start_index=0
    heapq.heappush(heap, [0,start_node])

    # we want an end board like this 9=blank space
    end_puzzle=[[j for j in range(i,i+len(start_node))] for i in range(1,len(start_node)**2+1, len(start_node))]
    visited = {}
    visited[str(start_node)]=None

    while heap[0][1] != end_puzzle : #min heap always has min in root
        if start_index%100000==0:
            print("time", start_index, time.time()-startTime)
        level,x=heapq.heappop(heap) 
        start_index+=1 
           
        for b in next_moves(x): 
            if str(b) not in visited:
                visited[str(b)]=x
                heapq.heappush(heap,[level+1,b])
    #construct BFS path by reversing order
    path =[]
    curr=end_puzzle
    while curr is not None:
        path.append(curr)
        curr=visited[str(curr)]
    path.reverse()
    for p in path:
        print_board(p)
    endTime = time.time()
    print("total Time = ", endTime-startTime)

def heuristic(board):
    #return a number related to how close you are to end position
    h=0
    for row in range(len(board)):
        for col in range(len(board[0])):
            #print(board[row][col])
            #figure out where number was supposed to go
            if board[row][col] != len(board)**2:
                spot_row = (board[row][col]-1)//len(board)  # 1//3=>0 1st row 2//3 =>0 3//3=>1
                spot_col = (board[row][col]-1)%len(board)
                
                h+= abs(spot_row - row) + abs(spot_col - col)
    #print('heuristic=',h)
    return h

def A_star(start_node):
    #will use a priority queue instead of queue
    startTime = time.time()
    heap = []
    start_index=0
    heapq.heappush(heap, [0 + heuristic(start_node),start_node])

    # we want an end board like this 9=blank space
    end_puzzle=[[j for j in range(i,i+len(start_node))] for i in range(1,len(start_node)**2+1, len(start_node))]
    visited = {}
    visited[str(start_node)]=None

    while heap[0][1] != end_puzzle : #min heap always has min in root
        if start_index%100000==0:
            print("time", start_index, time.time()-startTime)
        level,x=heapq.heappop(heap) 
        start_index+=1 
           
        h=heuristic(x)
        for b in next_moves(x): 
            if str(b) not in visited:
                visited[str(b)]=x
                heapq.heappush(heap,[level - h+1+heuristic(b),b])
    #construct BFS path by reversing order
    path =[]
    curr=end_puzzle
    while curr is not None:
        path.append(curr)
        curr=visited[str(curr)]
    path.reverse()
    step=1
    for p in path:
        print("*****STEP",step)
        step+=1
        print_board(p)
    endTime = time.time()
    print("total Time = ", endTime-startTime)

def BFS(start_node):
    startTime = time.time()
    queue = []
    start_index=0
    queue.append(start_node)

    # we want an end board like this 9=blank space
    end_puzzle=[[j for j in range(i,i+len(start_node))] for i in range(1,len(start_node)**2+1, len(start_node))]
    visited = {}
    visited[str(start_node)]=None

    while queue[start_index] != end_puzzle :
        if start_index%100000==0:
            print("time", start_index, time.time()-startTime)
        x=queue[start_index]
        start_index+=1 
           
        for b in next_moves(x): 
            if str(b) not in visited:
                visited[str(b)]=x
                queue.append(b)
    #construct BFS path by reversing order
    path =[]
    curr=end_puzzle
    while curr is not None:
        path.append(curr)
        curr=visited[str(curr)]
    path.reverse()
    for p in path:
        print_board(p)
    endTime = time.time()
    print("total Time = ", endTime-startTime)
        
print("begin_puzzle", begin_puzzle)
print("******beginning board****")
print_board(begin_puzzle)
print("************************")
A_star(begin_puzzle)
