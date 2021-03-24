continuar = True
while continuar:
    print()
    numero = int(input('insira um número: '))
    
    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')

    continuarResposta = input("inserir outro número? [S]im: ")
    continuar = continuarResposta.upper() == 'S'
    