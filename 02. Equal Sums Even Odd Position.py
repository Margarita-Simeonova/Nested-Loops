def check_number(num):
    digits = [int(d) for d in str(num)]
    even_sum = digits[1] + digits[3] + digits[5]  # Positions 2, 4, 6 (1-based)
    odd_sum = digits[0] + digits[2] + digits[4]    # Positions 1, 3, 5 (1-based)
    return even_sum == odd_sum

start = int(input())
end = int(input())

result = []
for num in range(start + 1, end):
    if check_number(num):
        result.append(str(num))

if result:
    print(' '.join(result))
