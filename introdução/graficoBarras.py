# %%
import matplotlib.pyplot as plt

# %%
x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 9, 4 ]

x2 = [2, 4, 6, 8, 10]
y2 = [8, 5, 3, 6, 2 ]


titulo = 'Gráfico de barras 2'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# "plt.plot(x, y)" deixa o grafico em linha

plt.bar(x1, y1, label='Grupo 1')
plt.bar(x2, y2, label='Grupo 2')
plt.legend()

plt.show()


# %%
