import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 10

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

print(f'menor valor: {min(vetor)}')
print(f'maior valor: {max(vetor)}')
