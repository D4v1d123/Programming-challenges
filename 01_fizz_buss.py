# Write a program that shows through the console (with a print) the
# numbers from 1 to 100 (both included and with a line break between
# each print), replacing the following:
# - Multiples of 3 for the word "fizz".
# - Multiples of 5 for the word "buzz".
# - Multiples of 3 and 5 at the same time for the word "fizzbuzz".

for num in range(101):
    print(num, end=" ")

    if num % 3 == 0: 
        print("fizz", end="")

    if num % 5 == 0:
        print("buzz", end="")

    print("\n")

