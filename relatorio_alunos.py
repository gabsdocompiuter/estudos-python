class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def set_notas(self, notas):
        self.notas = notas

    def get_nota_total(self):
        total = 0
        for nota in self.notas:
            total += nota
        return total / len(self.notas)

def carrega_aluno():
    nome = input('Insira o nome do aluno: ')

    notas = []
    notas.append(float(input('Insira a 1ª nota do aluno: ')))
    notas.append(float(input('Insira a 2ª nota do aluno: ')))
    notas.append(float(input('Insira a 3ª nota do aluno: ')))

    aluno = Aluno(nome)
    aluno.set_notas(notas)

    return aluno

def imprime_alunos(alunos):
    print('┌---- Nome ----┬---- Nota ----┐')

    for aluno in alunos:
        nome_relatorio = aluno.nome.ljust(14)
        nota_relatorio = f'{aluno.get_nota_total():.2f}'.ljust(14)
        print(f'|{nome_relatorio}|{nota_relatorio}|')

    print('└--------------┴--------------┘')


#-------------------------------------------------------------------
continuar = True
alunos = []
while continuar:
    print()
    alunos.append(carrega_aluno())

    input_continuar = input('Inserir outro aluno? ([S]im): ')
    continuar = (input_continuar == 'S' or input_continuar == 's')

imprime_alunos(alunos)
