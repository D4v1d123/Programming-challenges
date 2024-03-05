# Create a program that counts how many times is repeated each word
# and show the final count of all of them.
# - Punctuation marks are not part of the word.
# - A word is the same even it appear in upper and lower case.
# - You can not use language own functions that resolve it automatically.

from re import sub

# Regex (Regular expression) => It allow you to search, analyze and modify strings through of patterns.
# sub() => Replace a found pattern with other characters specified.

def counting_words(text): 
    repeated_words = {}

    for term in text.upper().split(" "):
        word = sub("[-.,:;_¡!¿?*@#(){}/<>]", "", term) # Remove puntuation marks from the word.

        if word in repeated_words:
            repeated_words[word] += 1
        else:
            repeated_words[word] = 1

    for key in repeated_words:
        print(f"The \"{key}\" was repeat {repeated_words.get(key)} {"time" if repeated_words.get(key) == 1 else "times"}.")


counting_words("Regular expresions: Regular expresions are patterns used to match combinations of characters in strings.")