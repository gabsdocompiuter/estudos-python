def recebe_valor(max, min=0):
    valor_valido = False
    while not valor_valido:
        try:
            user_input = int(input(f'insira um número entre {min} e {max}: '))
            if user_input < min or user_input > max:
                print('valor fora dos limites')
            else:
                return user_input
        except:
            print('você deve informar um número inteiro')

vetor = []

for i in range(0, 10):
    vetor.append(recebe_valor(50))

vetor_impares = []
for item in vetor:
    if item % 2 != 0:
        vetor_impares.append(item)

print(vetor)
print(vetor_impares)