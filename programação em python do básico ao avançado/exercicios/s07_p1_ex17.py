import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 10

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

for index, item in enumerate(vetor):
    if item < 0:
        vetor[index] = 0

print(vetor)