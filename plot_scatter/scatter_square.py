import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, edgecolors='None', c=y_value, cmap=plt.cm.Reds, s=14)

#Define e personaliza titulo e eixos
plt.title('Square Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#Personaliza os eixos
plt.tick_params(axis='both', labelsize=10)

#Define o tamanho dos eixos
plt.axis([0, 1001, 0, 1000001])

plt.savefig('scatter_square.png', bbox_inches='tight')