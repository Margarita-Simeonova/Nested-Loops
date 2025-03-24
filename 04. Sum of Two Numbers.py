# Read input values
start = int(input())
end = int(input())
magic_number = int(input())

# Initialize variables
combination_count = 0
found = False

# Iterate through all possible pairs in the interval
for first in range(start, end + 1):
    for second in range(start, end + 1):
        combination_count += 1
        if first + second == magic_number:
            print(f"Combination N:{combination_count} ({first} + {second} = {magic_number})")
            found = True
            break
    if found:
        break

# If no combination was found
if not found:
    print(f"{combination_count} combinations - neither equals {magic_number}")