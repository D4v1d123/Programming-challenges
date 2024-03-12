# Write a program that prints the first 50 numbers of the Fibonacci
# sequence starting at 0.
# - The Fibonacci series is made for a succession of numbers in which
#   the next one is always the sum of the two previous ones.
#   0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci (last_series):
    value_1 = 0
    value_2 = 1

    for serie in range(last_series + 1):
        print(value_1)
        
        aux = value_2
        value_2 = value_1 + value_2
        value_1 = aux

fibonacci(50)