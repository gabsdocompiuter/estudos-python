vetor = list(range(1, 7))

# a
vetor.extend([1, 0, 5, -2, -5, 7])

# b
soma = vetor[0] + vetor[1] + vetor[5]
print(f'soma: {soma}')

# c
vetor[3] = 100

# d
for i in vetor:
    print(i)
