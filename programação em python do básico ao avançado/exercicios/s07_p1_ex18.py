import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 10

vetor = functions.monta_vetor_int(TAMANHO_VETOR)

user_input = int(input('insira um número: '))

for item in vetor:
    if item % user_input == 0:
        print(f'{item} é multiplo de {user_input}')