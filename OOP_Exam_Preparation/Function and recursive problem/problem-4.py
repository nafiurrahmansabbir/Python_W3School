#Write a Python function to check if a given string is a palindrome recursively.
def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])


string = input("Enter a words : ")
result=is_palindrome(string);
if result==True:
    print ("The word", string, "is a palindrome.")
else:
    print("The word ", string, "is not a palindrome.")
