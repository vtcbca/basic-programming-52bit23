def fibonacci_up_to_max_value(max_value):
    fib_sequence = []
    a, b = 0, 1
    while a < max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# Example usage
max_value = 50
print(fibonacci_up_to_max_value(max_value))
