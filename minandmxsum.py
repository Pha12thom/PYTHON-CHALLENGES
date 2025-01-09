def minAndmaxofArray(arr):
    minSum = 0
    maxSum = 0
    arr.sort()
    for i in range(len(arr)-1):
        print("min i",i)
        minSum += arr[i]
    for i in range(1, len(arr)):
        print("max i",i)
        maxSum += arr[i]
    #print(minSum, maxSum)
# Sample Input 0
arr = [1, 2, 3, 4, 5]
minAndmaxofArray(arr)  # Output: 10 14

    