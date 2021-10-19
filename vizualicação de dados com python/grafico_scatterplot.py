import matplotlib.pyplot as plt

x = list(range(1, 6))
y = [10, 8, 7, 5.5, 9]

plt.title("Grafico Teste")
plt.xlabel("Provas")
plt.ylabel("Notas")

plt.scatter(x, y, label="Notas")
plt.plot(x, y)

plt.legend()
plt.show()