def staircase(n):
    for i in range(n+1):
        print(' ' * (n - i) + '#' * i)

# Example usage
staircase(5)
