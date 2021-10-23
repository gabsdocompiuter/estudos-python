import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 6

vetor = functions.monta_vetor_int(TAMANHO_VETOR)
vetor.reverse()

print(vetor)
