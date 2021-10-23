import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 5

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

# remove elementos duplicados
vetor = list(dict.fromkeys(vetor))

print(vetor)
