import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [10, 8, 7, 5.5, 10]

x2 = [2, 4, 6, 8, 10]
y2 = [8, 9, 5, 7, 9]

plt.title("Grafico Teste")
plt.xlabel("Provas")
plt.ylabel("Notas")

plt.bar(x1, y1, label="Grupo 1")
plt.bar(x2, y2, label="Grupo 2")
plt.legend()
plt.show()