import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 5

vetor = functions.monta_vetor_float(TAMANHO_VETOR)
user_input = input('insira uma opção: ')

if user_input == '1':
    print(vetor)

elif user_input == '2':
    vetor.reverse()
    print(vetor)

elif user_input == '0':
    pass

else:
    print('opção inválida')