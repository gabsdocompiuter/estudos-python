continuar = True
while continuar:
    print()
    numero = int(input('insira um número: '))
    
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')

    continuar_resposta = input("inserir outro número? [S]im: ")
    continuar = continuar_resposta.upper() == 'S'
    