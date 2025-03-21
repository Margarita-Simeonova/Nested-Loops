def combinations(numb):
    counter = 0
    for i in range(numb + 1):
        for j in range(numb + 1):
            for k in range(numb + 1):
                result = i + j + k
                if result == numb:
                    counter += 1
    return counter


number = int(input())
print(combinations(number))
