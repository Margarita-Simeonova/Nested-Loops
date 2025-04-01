def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


prime_sum = 0
non_prime_sum = 0

while True:
    user_input = input().strip()

    if user_input.lower() == "stop":
        break

    try:
        num = int(user_input)
    except ValueError:
        continue  # ignore non-integer inputs

    if num < 0:
        print("Number is negative.")
        continue

    if is_prime(num):
        prime_sum += num
    else:
        non_prime_sum += num

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
