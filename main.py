def max_power(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]  # Initialize dp matrix
    path = [[''] * n for _ in range(n)]  # Initialize path matrix

    # Find the starting position with maximum power
    max_power = float('-inf')
    start_row = None
    start_col = None
    
    # Iterate through the first column
    for i in range(n):
        dp[i][0] = grid[i][0]
        if dp[i][0] > max_power:
            max_power = dp[i][0]
            start_row = i
            start_col = 0
        path[i][0] = 'U'  # Up

    # Iterate through the last row
    for j in range(1, n):
        dp[n-1][j] = grid[n-1][j] + dp[n-1][j-1]
        if dp[n-1][j] > max_power:
            max_power = dp[n-1][j]
            start_row = n - 1
            start_col = j
        path[n-1][j] = 'R'  # Right

    # Fill the dp matrix
    for i in range(n - 2, -1, -1):
        for j in range(1, n):
            if dp[i+1][j] - 2 > dp[i][j-1] - 1:
                dp[i][j] = dp[i+1][j] - 2 + grid[i][j]  # Penalty of -2 for moving up
                path[i][j] = 'U'  # Up
            else:
                dp[i][j] = dp[i][j-1] - 1 + grid[i][j]  # Penalty of -1 for moving right
                path[i][j] = 'R'  # Right

            # Update starting position if a higher power is found
            if dp[i][j] > max_power:
                max_power = dp[i][j]
                start_row = i
                start_col = j

    # Visualize the optimal path
    row, col = start_row, start_col
    path_matrix = [['.'] * n for _ in range(n)]  # Initialize the path matrix
    while row != n - 1 or col != 0:
        path_matrix[row][col] = 'X'  # Mark the cell as part of the optimal path
        if path[row][col] == 'U':
            row += 1
        else:
            col -= 1
    path_matrix[row][col] = '0'  # Mark the starting cell
    
    return max_power, path_matrix

# Example grid
grid = [
    [-10, -300, -100, -300, -50, -600, -700, -800, -900, -100, -101, -102, -103, -140, -150, -106, -107, -108, -109, -2000],
    [1, -200, -400, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 0, -2, -13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 1, 1, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 3, 10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, -200, -400, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 0, -2, -13, 5, 6, 7, 8000, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 1, 1, 1, 500000, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 3, 10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, -200, -400, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 0, -2, -13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 1, 1, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 3, 10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, -200, -400, 1, 5, 6, 7, 8, 9, 10000, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 0, -2, -13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 1, 1, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 3, 10, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, -200, -400, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 0, -2, -13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 1, 1, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, -14, 15, 16, 17, 18, 19, 20]
]

max_power_value, path_matrix = max_power(grid)

# Reverse path_matrix to display in the correct orientation
# path_matrix = path_matrix[::-1]

print("Maximum power:", max_power_value)
print("Optimal Path:")
for row in path_matrix:
    print(' '.join(row))
