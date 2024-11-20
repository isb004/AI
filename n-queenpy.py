def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at position (row, col)."""
    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    """Solve the N-Queens problem recursively."""
    if row == n:
        print_board(board)  # Print the board when a solution is found
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q"  # Place the queen
            solve_n_queens(board, row + 1, n)  # Recur for the next row
            board[row][col] = "."  # Backtrack by removing the queen


def n_queens(n):
    """Initialize the board and start solving."""
    board = [["." for _ in range(n)] for _ in range(n)]  # Create an empty board
    solve_n_queens(board, 0, n)


if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    n_queens(n)
