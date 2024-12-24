n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    spaces = " " * (n - i) * 2
    numbers = " ".join(str(j) for j in range(1, 2 * i))
    print(spaces + numbers)
