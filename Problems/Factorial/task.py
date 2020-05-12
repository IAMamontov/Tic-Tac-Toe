n_given = int(input())
iterator = 0
factorial = 1
while iterator < n_given:
    iterator += 1
    factorial *= iterator
print(factorial)