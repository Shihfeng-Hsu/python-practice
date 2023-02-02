def is_solved(board):
    # TODO: Check if the board is solved!

    all_result_arr=[]

    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            all_result_arr.append(board[i][j])
        for j in range(0,len(board[i])):
            all_result_arr.append(board[j][i]) 
    for i in range(0,len(board)):
        all_result_arr.append(board[i][i])
    all_result_arr.append(board[0][2])
    all_result_arr.append(board[1][1])
    all_result_arr.append(board[2][0])


    print(all_result_arr)
    
    for i in range(0,len(all_result_arr),3):
        if all_result_arr[i] == 1 and all_result_arr[i+1] == 1 and all_result_arr[i+2] == 1:
            print(1)
            return 1
        elif all_result_arr[i] == 2 and all_result_arr[i+1] == 2 and all_result_arr[i+2] == 2:
            print(2)
            return 2
    if 0 in all_result_arr:
        print(-1)
        return -1
    print(0)
    return 0
    # not yet finished

'''
Other solution
I think this is not great than mine.

def isSolved(board):
	for i in range(0,3):
		if board[i][0] == board[i][1] == board[i][2] != 0:
			return board[i][0]
		elif board[0][i] == board[1][i] == board[2][i] != 0:
			return board[0][i]
			
	if board[0][0] == board[1][1] == board[2][2] != 0:
		return board[0][0]
	elif board[0][2] == board[1][1] == board[2][0] != 0:
		return board[0][0]

	elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
		return 0
	else:
		return -1
'''


board1 = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]]
is_solved(board1)#, -1)

# winning row
board2 = [[1, 1, 1],
         [0, 2, 2],
         [0, 0, 0]]
is_solved(board2)#, 1)

# winning column
board3 = [[2, 1, 2],
         [2, 1, 1],
         [1, 1, 2]]
is_solved(board3)#, 1)

# # draw
board4 = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]
is_solved(board4)#, 0)

'''
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

'''