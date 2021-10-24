vetor = []

for i in range(0, 50):
    valor = (i + 5 * i) % (i + 1)
    vetor.append(valor)

print(vetor)