class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def setNotas(self, notas):
        self.notas = notas

    def getNotaTotal(self):
        total = 0
        for nota in self.notas:
            total += nota
        return total / len(self.notas)

def carregaAluno():
    nome = input('Insira o nome do aluno: ')

    notas = []
    notas.append(float(input('Insira a 1ª nota do aluno: ')))
    notas.append(float(input('Insira a 2ª nota do aluno: ')))
    notas.append(float(input('Insira a 3ª nota do aluno: ')))

    aluno = Aluno(nome)
    aluno.setNotas(notas)

    return aluno

def imprimeAlunos(alunos):
    print('┌---- Nome ----┬---- Nota ----┐')

    for aluno in alunos:
        nomeRelatorio = aluno.nome.ljust(14)
        notaRelatorio = str(aluno.getNotaTotal()).ljust(14)
        print(f'|{nomeRelatorio}|{notaRelatorio}|')

    print('└--------------┴--------------┘')


#-------------------------------------------------------------------
continuar = True
alunos = []
while continuar:
    print()
    alunos.append(carregaAluno())

    inputContinuar = input('Inserir outro aluno? ([S]im): ')
    continuar = (inputContinuar == 'S' or inputContinuar == 's')

imprimeAlunos(alunos)
