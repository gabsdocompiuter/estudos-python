import matplotlib.pyplot as plt

nome_arquivo = "populacao_brasileira.csv"

anos = []
populacoes = []

with open(nome_arquivo) as arquivo:
    for linha in arquivo:
        l = linha.rstrip().split(';')

        if l[0] == 'ano':
            continue

        ano = l[0]
        populacao = l[1]

        anos.append(ano)
        populacoes.append(int(populacao))

plt.table("Crescimento da população brasileira")
plt.xlabel("Ano")
plt.ylabel("População")

plt.bar(anos, populacoes)

plt.show()