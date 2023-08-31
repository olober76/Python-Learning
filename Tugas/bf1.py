import time
def is_safe(board, row, col):
    # Memeriksa apakah ratu pada posisi (row, col) aman
    # pada papan catur yang sudah ada
    
    # Memeriksa baris yang sama
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Memeriksa diagonal atas kiri
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Memeriksa diagonal bawah kiri
    i = row
    j = col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    return True


def solve_n_queen(board, col):
    # Basis rekursif: jika semua ratu telah ditempatkan
    if col >= len(board):
        return True
    
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Menempatkan ratu pada posisi (i, col)
            board[i][col] = 1
            
            # Memanggil rekursif untuk menempatkan ratu pada kolom berikutnya
            if solve_n_queen(board, col + 1):
                return True
            
            # Jika tidak ada solusi yang ditemukan, kembali ke 0 dan coba baris berikutnya
            board[i][col] = 0
    
    # Jika tidak ada baris yang memungkinkan pada kolom ini, kembalikan False
    return False


def print_solution(board):
    # Mencetak solusi papan catur
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()


def solve_n_queen_problem(n):
    # Membuat papan catur berukuran n x n
    board = [[0] * n for _ in range(n)]
    
    if solve_n_queen(board, 0):
        print_solution(board)
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
