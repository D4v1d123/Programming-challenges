# Write a function that calculates and returns the factorial of a given number
# of recursive form. 

def factorial (number):
    if number == 1: return 1
    return ("Number must be greater than 0.") if (number < 0) else (number * factorial(number - 1))


print(factorial(4))
print(factorial(-2))