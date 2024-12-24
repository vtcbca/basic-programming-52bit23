n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    spaces = " " * (n - i) * 2
    first_half = [chr(64 + j) for j in range(1, i + 1)]
    second_half = [chr(64 + j) for j in range(i - 1, 0, -1)]
    print(spaces + " ".join(first_half + second_half))