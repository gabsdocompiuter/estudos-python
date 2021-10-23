import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 10

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

numeros_negativos = 0
soma_numeros_positivos = 0
for item in vetor:
    if item < 0:
        numeros_negativos += 1
    else:
        soma_numeros_positivos += item

print(f'quantidade itens negativos: {numeros_negativos}')
print(f'soma dos números positivos: {soma_numeros_positivos}')
