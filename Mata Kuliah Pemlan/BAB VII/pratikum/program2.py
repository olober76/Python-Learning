x = y = 0
def maze(length, width, x, y):
    
    dp = [[0 for _ in range(width)] for _ in range(length)]
    dp[0][0] = 1
    
    for i in range(length):
        for j in range(width):
            if i != 0 or j != 0:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[length-1][width-1]

tinggi = int(input("Tinggi maze : "))
lebar = int(input("Lebar maze : "))
print(maze(tinggi, lebar, x, y))
