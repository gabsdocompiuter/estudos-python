import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 8

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

indice_1 = int(input(f'escolha uma posição do vetor (1 - {TAMANHO_VETOR}): '))
indice_2 = int(input(f'escolha outra posição do vetor (1 - {TAMANHO_VETOR}): '))

soma = vetor[indice_1 - 1] + vetor[indice_2 - 1]

print(f'a soma das duas posições é {soma}')
