# Write a program that will check if two strings are palindromes.
#A palindrome is a word that spells the same forward and backward.
#Palindrome: a word, phrase, or sequence that reads the same backward as
#forward, examples for valid palindromes: madam, nurses run.

def is_palindrome(string):
    cleaned_string = string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]


first_str = "Madam"
second_str = "Java"

if is_palindrome(first_str):
    print(f"'{first_str}' is a palindrome.")
else:
    print(f"'{first_str}' is not a palindrome.")

if is_palindrome(second_str):
    print(f"'{second_str}' is a palindrome.")
else:
    print(f"'{second_str}' is not a palindrome.")
