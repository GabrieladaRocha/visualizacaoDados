# %%
import matplotlib.pyplot as plt

# %%
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 9, 4 ]


titulo = 'Gráfico de Linha'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

plt.plot(x1, y1)
plt.show()



# %%
