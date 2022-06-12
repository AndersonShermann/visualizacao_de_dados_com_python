import matplotlib.pyplot as plt

input_valores = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_valores, squares, linewidth=5, c='Red')

#Define o titulo do gráfico e nomeia os eixos
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square Value', fontsize=14)

#Estiliza as informações dos eixos
plt.tick_params(axis='both', labelsize=14)

#Define o limite dos eixos
plt.axis([1, 5, 1, 30])

plt.savefig('square.png', bbox_inches='tight')