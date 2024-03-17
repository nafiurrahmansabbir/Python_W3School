#Write a Python function to reverse a string recursively.
def reverse_string_recursive(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

string = input("Enter a String : ")
print("Original string:", string)
print("Reversed string:", reverse_string_recursive(string))
