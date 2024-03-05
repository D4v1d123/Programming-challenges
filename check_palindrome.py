# Write a function that receives a text and returns true or false
# (Boolean) depending on whether this is a palindrome or not. 
# - A palindrome is a word or expression that is same if read
# from left to right that from right to left.
# - Space, punctuation marks and accents are NOT taken into 
# account.
# Example: Sit on a potato pan, Otis

from re import sub
from unidecode import unidecode

def check_palindrome (text):
    word = sub("[ -.,:;_¡!¿?*@#(){}/<>]", "", text.lower()) # Remove 
    # punctuation marks and spaces.
    word = unidecode(word) # Replace accents.
    
    return word == word [:: -1]

print(check_palindrome("Sit on a potato pan, Otis"))
print(check_palindrome("A dog! A panic in a pagoda!"))
print(check_palindrome("A Toyota's Toyota"))