from statistics import mean

import util.functions as functions

functions.clear_console()

TAMANHO_VETOR = 15

notas = functions.monta_vetor_float(TAMANHO_VETOR, input_message='insira a nota do aluno: ')

media_notas = mean(notas)
print(f'a médias das notas é {media_notas}')
