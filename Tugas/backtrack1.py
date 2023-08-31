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


def solve_n_queen_iterative(n):
    board = [-1] * n  # Inisialisasi papan catur dengan -1
    col = 0
    solutions = []

    while col >= 0:
        board[col] += 1

        while board[col] < n and not is_safe(board, board[col], col):
            board[col] += 1

        if board[col] < n:
            if col == n - 1:
                solutions.append(board[:])
            else:
                col += 1
                board[col] = -1
        else:
            col -= 1

    if solutions:
        for solution in solutions:
            print_solution(solution)
    else:
        print("Tidak ada solusi yang mungkin.")


N = int(input("Enter Number of queens: "))

start_time = time.time()

# Solve N Queen Problem with N = 8

solve_n_queen_iterative(N)


# Calculate the execution time
end_time = time.time()
execution_time = end_time - start_time

# Print the execution time
print("Execution time: {:.5f} seconds".format(execution_time))
# Menjalankan fungsi untuk N Queen Problem dengan N = 8