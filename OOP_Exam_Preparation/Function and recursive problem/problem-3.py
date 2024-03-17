#Write a Python function to calculate the power of a number recursively.
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base = int(input("Enter the base number : "))
exponent = int(input("Enter the exponent : "))
print("Result : ",power(base, exponent))
