import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 3

vetor_a = functions.monta_vetor_int(TAMANHO_VETOR, input_message='insira um número inteiro para o primeiro vetor: ')
vetor_b = functions.monta_vetor_int(TAMANHO_VETOR, input_message='insira um número inteiro para o segundo vetor: ')

vetor_c = [x + y for x, y in zip(vetor_a, vetor_b)]

print(vetor_a)
print(vetor_b)
print(vetor_c)
