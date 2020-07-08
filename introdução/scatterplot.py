# %%
import matplotlib.pyplot as plt

# %%
x2 = [2, 4, 6, 8, 10]
y2 = [8, 5, 3, 6, 2 ]


titulo = 'Scatterplot: Gráfico de Dispersão'
eixoX = 'Eixo X'
eixoY = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

# "plt.plot(x, y)" deixa o grafico em linha

plt.scatter(x2, y2, label='somente pontos', color="red")
plt.plot(x2, y2)
plt.legend()

#plt.show()
plt.savefig("figura1.pdf")

# %%
