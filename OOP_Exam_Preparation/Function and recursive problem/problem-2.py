#Write a Python function to find the sum of digits of a positive integer recursively.
def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


number = int(input("Enter a number : "))
print("Sum of digits of", number, "is:", sum_of_digits(number))
