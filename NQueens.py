def isSafe(board, row, col):
    for i in range(row): # Check if there is a queen in the same column
        if board[i][col] == 1:
            return False
        
    i, j = row, col
    while i >= 0 and j >= 0: # Check if there is a queen in the left diagonal
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < len(board[0]): # Check if there is a queen in the right diagonal
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def Nqueens(board, row):
    if row == len(board):
        print(board)
    for col in range(len(board[0])):
        if isSafe(board, row, col):
            board[row][col] = 1
            Nqueens(board, row + 1)
            board[row][col] = 0
        
n = int(input('Enter the number of queens: '))
board = [[0 for i in range(n)] for j in range(n)]
Nqueens(board, 0)