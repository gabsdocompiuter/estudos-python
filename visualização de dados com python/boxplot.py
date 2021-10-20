import matplotlib.pyplot as plt
import numpy as np

lista = np.random.randint(1, 5000, size=100)

plt.boxplot(lista)
plt.show()