def safe(board, row, col):
    for i in range(row):
        # same column
        if board[i] == col:
            return False
        # diagonal
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row):
    if row == len(board):
        print("Solution:", board)
        return
    
    for col in range(len(board)):
        if safe(board, row, col):
            board[row] = col
            solve(board, row + 1)


# size of board (change to 8 for classic problem)
n = 4
board = [-1] * n

solve(board, 0)