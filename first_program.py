# to check if a string is palidrome or not.

def is_palindrome(s:str) -> bool:
    return s == s[::-1]

s = input("Enter a string: ")
if is_palindrome(s):
    print(f"{s} is a palindrome!")
else:
    print(f"{s} is not a palindrome!")