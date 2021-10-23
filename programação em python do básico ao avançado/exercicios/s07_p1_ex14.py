import util.functions as functions
functions.clear_console()

TAMANHO_VETOR = 10

vetor = functions.monta_vetor_int(TAMANHO_VETOR)
elementos_duplicados = []

for item in vetor:
    repeticoes_elemento = vetor.count(item)

    if repeticoes_elemento > 1:
        item_inserido = next((elemento for elemento in elementos_duplicados if elemento['item'] == item), None)
        
        if not item_inserido:
            elementos_duplicados.append({
                'item': item,
                'repeticoes': repeticoes_elemento
            })

for elemento in elementos_duplicados:
    item = elemento['item']
    repeticoes = elemento['repeticoes']

    print(f'número {item} inserido {repeticoes} vezes')
    