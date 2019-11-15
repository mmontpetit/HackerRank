def diagonalDifference(arr):
    # Given a square matrix, calculate the absolute difference between the sums of its diagonals.
    primary = 0
    secondary = 0
    for i in range(len(arr)):
        primary += arr[i][i]
        secondary += arr[i][(len(arr)-i-1)]
    return abs(primary-secondary)