# Write a function that takes two words (String) and returns true or
# false (Bool) depending on whether or not they are anagrams.
# - An Anagram consists of forming a word by rearranging ALL the
# letters of another initial word.
# - It is NOT necessary to check that both words exist.
# - Two exactly the same words are not an anagram.

def is_anagram(word_1, word_2):
    if sorted(word_1.lower()) == sorted(word_2.lower()):
        return True
    
    return False


# It's an anagram
print(is_anagram("camion", "camino"))

# It's not an anagram
print(is_anagram("camino", "camilo"))
