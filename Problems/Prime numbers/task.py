prime_numbers = []
for i in range(2,1001):
    if all([i % j for j in range(2, i)]):
        prime_numbers.append(i)