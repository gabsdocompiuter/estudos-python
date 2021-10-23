from statistics import mean

import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 5

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

print(vetor)
print(f'maior elemento: {max(vetor)}')
print(f'menor elemento: {min(vetor)}')
print(f'média dos valores: {mean(vetor)}')
