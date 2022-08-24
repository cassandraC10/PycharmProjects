def string_palindrome(s):
    return s == s[::-1]


p = "wow"
palindrome = string_palindrome(p)

if palindrome:
    print("String is Palindrome")
else:
    print("Not Palindrome")
