import time
def print_solution(board):
    # Mencetak solusi papan catur
    for row in board:
        line = ["." for _ in range(len(board))]
        line[row] = "Q"
        print(" ".join(line))
    print()


def is_safe(board, row, col):
    # Memeriksa apakah ratu pada posisi (row, col) aman
    # pada papan catur yang sudah ada
    
    for i in range(col):
        # Memeriksa baris yang sama
        if board[i] == row:
            return False
        
        # Memeriksa diagonal
        if abs(board[i] - row) == abs(i - col):
            return False
    
    return True


def solve_n_queen_recursive(board, col, solutions):
    if col >= len(board):
        solutions.append(board[:])
        return

    for row in range(len(board)):
        if is_safe(board, row, col):
            board[col] = row
            solve_n_queen_recursive(board, col + 1, solutions)

    board[col] = -1


def solve_n_queen(n):
    board = [-1] * n  # Inisialisasi papan catur dengan -1
    solutions = []

    solve_n_queen_recursive(board, 0, solutions)

    if solutions:
        for solution in solutions:
            print_solution(solution)
    else:
        print("Tidak ada solusi yang mungkin.")


N = int(input("Enter Number of queens: "))

start_time = time.time()

# Solve N Queen Problem with N = 8

solve_n_queen(N)


# Calculate the execution time
end_time = time.time()
execution_time = end_time - start_time

# Print the execution time
print("Execution time: {:.5f} seconds".format(execution_time))
