def hourglassSum(arr):
    hourglass=[]
    for i in range(len(arr)-2):

        for x in range(len(arr)-2):
            hourglass.append(sum(arr[i][x:x+3]+arr[i+2][x:x+3])+arr[i+1][x+1])

    return max(hourglass)
