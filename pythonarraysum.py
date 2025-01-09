def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1

    return [alice_score, bob_score]

# Sample Input 0
a = [5, 6, 7]
b = [3, 6, 10]
print(compareTriplets(a, b))  # Output: [1, 1]

# Sample Input 1
a = [17, 28, 30]
b = [99, 16, 8]
print(compareTriplets(a, b))  # Output: [2, 1]

def addDiagonalsofMatrix(arr):
    n = len(arr)
    left_diagonal_sum = 0
    right_diagonal_sum = 0

    for i in range(n):
        left_diagonal_sum += arr[i][i]
        right_diagonal_sum += arr[i][n - i - 1]

    return abs(left_diagonal_sum - right_diagonal_sum)

def print3by3Matrix(arr):
    for i in range(3):
        for j in range(3):
            print(arr[i][j], end=" ")
        print()
        