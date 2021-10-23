import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 5

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

maior_valor = max(vetor)
indice_maior_elemento = vetor.index(maior_valor)

menor_valor = min(vetor)
indice_menor_elemento = vetor.index(menor_valor)

print(f'maior valor: {maior_valor}')
print(f'posição: {indice_maior_elemento + 1}')

print(f'menor valor: {menor_valor}')
print(f'posição: {indice_menor_elemento + 1}')
