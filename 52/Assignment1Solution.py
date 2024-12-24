def factorial_using_recursion(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_using_recursion(n - 1)

# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial_using_recursion(number)}")
