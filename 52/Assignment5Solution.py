def is_palindrome_loop(input_string):
    left = 0
    right = len(input_string) - 1
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1
    return True

# Example usage
input_string = "madam"
print(is_palindrome_loop(input_string))  # Output: True
