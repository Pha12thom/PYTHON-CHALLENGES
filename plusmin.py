def plusMinus(arr):
    # Write your code here
    #loop through array arr[i]
    #if arr < 0 countNeg += 1 else arr[i] = 0 countO += 1 else arr[i] > 0 countPov += 1
    # den = len(arr)
    countNeg = 0
    countO = 0
    countPov = 0
    den = len(arr)
    for i in range(den):
        if arr[i] < 0:
            countNeg += 1
            countNeg += 1
        elif arr[i] == 0:
            countO += 1
            fractO = countO/den
            countO += 1
            countPov += 1
            fractPov = countPov/den
            print(format(fractPov, '.6f')) 