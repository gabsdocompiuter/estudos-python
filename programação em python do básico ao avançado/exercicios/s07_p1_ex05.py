import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 10

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

numeros_pares = 0
for item in vetor:
    if item % 2 == 0:
        numeros_pares += 1

print(numeros_pares)
