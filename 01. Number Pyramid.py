n = int(input())
current_num = 1
row_length = 1

while current_num <= n:
    # Print numbers for current row
    for _ in range(row_length):
        if current_num > n:
            break
        print(current_num, end=' ')
        current_num += 1

    print()  # New line after each row
    row_length += 1
