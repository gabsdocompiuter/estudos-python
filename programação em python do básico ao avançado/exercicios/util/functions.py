import os

from typing import List

clear_console = lambda: os.system('cls')

def monta_vetor_int(tamanho: int, input_message='') -> List:
    if input_message == '':
        input_message = 'insira um número inteiro: '

    vetor = []

    for i in range(0, tamanho):
        user_input = int(input(input_message))
        vetor.append(user_input)
    
    return vetor

def monta_vetor_float(tamanho: int, input_message='') -> List:
    if input_message == '':
        input_message = 'insira um número inteiro: '

    vetor = []

    for i in range(0, tamanho):
        user_input = float(input(input_message))
        vetor.append(user_input)
    
    return vetor