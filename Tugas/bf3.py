import time
def is_safe(board, row, col):
    # Memeriksa apakah ratu pada posisi (row, col) aman
    # pada papan catur yang sudah ada
    
    # Memeriksa baris yang sama
    for i in range(col):
        if board[i] == row or board[i] - row == i - col or board[i] - row == col - i:
            return False
    
    return True


def solve_n_queen(board, col, solutions):
    # Basis rekursif: jika semua ratu telah ditempatkan
    if col >= len(board):
        solutions.append(board[:])
        return
    
    for row in range(len(board)):
        if is_safe(board, row, col):
            # Menempatkan ratu pada posisi (row, col)
            board[col] = row
            
            # Memanggil rekursif untuk menempatkan ratu pada kolom berikutnya
            solve_n_queen(board, col + 1, solutions)


def print_solution(board):
    # Mencetak solusi papan catur
    for row in board:
        line = ["." for _ in range(len(board))]
        line[row] = "Q"
        print(" ".join(line))
    print()


def solve_n_queen_problem(n):
    # Membuat papan catur berukuran n x n
    board = [0] * n
    solutions = []
    
    solve_n_queen(board, 0, solutions)
    
    if solutions:
        for solution in solutions:
            print_solution(solution)
    else:
        print("Tidak ada solusi yang mungkin.")

N = int(input("Enter Number of queens: "))

start_time = time.time()

# Solve N Queen Problem with N = 8

solve_n_queen_problem(N)


# Calculate the execution time
end_time = time.time()
execution_time = end_time - start_time

# Print the execution time
print("Execution time: {:.5f} seconds".format(execution_time))
# Menjalankan fungsi untuk N Queen Problem dengan N = 8