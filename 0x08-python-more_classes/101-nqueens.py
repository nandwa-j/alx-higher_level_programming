#!/usr/bin/python3
"""N queens puzzle"""

import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]"""

    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, n, solutions):
    """Utility function to solve N queens"""

    # If all queens are placed, append the solution to the solutions list
    if col == n:
        sol = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    sol.append([i, j])
        solutions.append(sol)
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_n_queens_util(board, col + 1, n, solutions)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0


def solve_n_queens(n):
    """Solve the N queens problem and print all solutions"""

    # Initialize empty board
    board = [[0] * n for _ in range(n)]
    solutions = []

    # Start from the leftmost column and recursively solve the problem
    solve_n_queens_util(board, 0, n, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./101-nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for sol in solutions:
        print(sol)
