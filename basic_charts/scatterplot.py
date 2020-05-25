import matplotlib.pyplot as plt

x = [1, 3, 5, 7 ,9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]

titulo = "Scatterplot: Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.plot(x, y, color="k", linestyle="--")
plt.legend()
plt.show()

#Salvar imagem na pasta corrente (Possivel salver em PDF)
#dpi configura resolução
#plt.savefig("figura1.png", dpi=300)