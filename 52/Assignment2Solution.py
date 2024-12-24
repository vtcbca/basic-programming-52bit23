def is_prime_all(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Example usage
number = int(input("Enter a number: "))
if is_prime_all(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
