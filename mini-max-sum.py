def miniMaxSum(arr):
    # Given five positive integers, find the minimum and maximum values that can be 
    # calculated by summing exactly four of the five integers. 
    Sum = []

    for i in list(arr):
        item_removed = arr[0]
        arr.remove(i)
        Sum.append(sum(arr))
        arr.append(item_removed)
        
    print(min(Sum),max(Sum))

    or 

    def miniMaxSum(arr):
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
        print ( sum-max(arr), sum-min(arr))