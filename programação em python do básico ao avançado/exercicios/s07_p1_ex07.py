import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 10

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

maior_valor = max(vetor)
indice_maior_elemento = vetor.index(maior_valor)

print(f'maior valor: {maior_valor}')
print(f'posição: {indice_maior_elemento + 1}')
