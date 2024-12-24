def reverse_string_recursive(input_string):
    if len(input_string) == 0:
        return input_string
    return reverse_string_recursive(input_string[1:]) + input_string[0]

# Example usage
input_string = "Hello, World!"
print(reverse_string_recursive(input_string))
