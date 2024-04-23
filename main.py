import sys
import numpy as np
import pandas as pd

def max_power(grid):
    n = len(grid)
    dp_matrix = [[0] * n for _ in range(n)]  

  
    initial_power = 5

    max_power = float('-inf')
    start_row, start_col = None, None

    for i in range(n):
        dp_matrix[i][0] = grid[i][0] + initial_power - 1  
        if dp_matrix[i][0] > max_power:
            max_power = dp_matrix[i][0]
            start_row, start_col = i, 0


    for j in range(n):
        dp_matrix[n - 1][j] = grid[n - 1][j] + initial_power - 2
        if dp_matrix[n - 1][j] > max_power:
            max_power = dp_matrix[n - 1][j]
            start_row, start_col = n - 1, j


    for i in range(n - 2, -1, -1):
        for j in range(1, n):
            if dp_matrix[i + 1][j] - 2 > dp_matrix[i][j - 1] - 1 and i < n - 1: 
                dp_matrix[i][j] = dp_matrix[i + 1][j] + grid[i][j] - 2  # Penalty of -2 for moving up
            else:
                dp_matrix[i][j] = dp_matrix[i][j - 1] + grid[i][j] - 1  # Penalty of -1 for moving right

            if dp_matrix[i][j] > max_power:
                max_power = dp_matrix[i][j]  # To get maximum power 

  
    path = [(start_row, start_col)]

    i, j = start_row, start_col

    while i < n - 1 and j < n-1:
        if dp_matrix[i - 1][j] - 2 > dp_matrix[i][j + 1] - 1:
            i = i - 1 #moved up
            path.append((i,j))
        else:
            j = j + 1 #moved right
            path.append((i,j))

        

    return max_power, path




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Env_filename.xlsx not found")
        sys.exit(1)

    grid = np.asarray(pd.read_excel(sys.argv[1]))
    max_power_value, optimal_path = max_power(grid)

    print("Maximum power:", max_power_value)
    print("Optimal Path:", optimal_path)
