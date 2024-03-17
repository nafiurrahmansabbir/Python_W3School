#Write a Python function to find the greatest common divisor (GCD) of two numbers recursively using Euclid's algorithm.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

num1 = int(input("Enter  first number: "))
num2 = int(input("Enter second number: "))
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))
