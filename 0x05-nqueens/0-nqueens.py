#!/usr/bin/python3
import sys

def solve_nqueens(n):
    def is_attack(i, j):
        for k in range(0, n):
            if board[i][k] == 1 or board[k][j] == 1:
                return True
        for k in range(0, n):
            for l in range(0, n):
                if (k + l == i + j) or (k - l == i - j):
                    if board[k][l] == 1:
                        return True
        return False

    def place_queen(n, curr_board):
        if curr_board == n:
            return True
        for i in range(0, n):
            if not(is_attack(curr_board, i)):
                board[curr_board][i] = 1
                if place_queen(n, curr_board + 1):
                    return True
                board[curr_board][i] = 0
        return False

    board = [[0]*n for _ in range(n)]
    place_queen(n, 0)
    return board

def print_board(board):
    queens = [[i, j] for i in range(n) for j in range(n) if board[i][j] == 1]
    print(queens)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)

board = solve_nqueens(n)
print_board(board)