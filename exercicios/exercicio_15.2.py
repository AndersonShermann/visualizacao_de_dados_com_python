#   Cubos coloridos: Aplique um colormap em seu gráfico de cubos.
import  matplotlib.pyplot as plt

x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]

#Plota e personaliza os valores de x e y
plt.scatter(x_value, y_value, edgecolors='None', c=y_value, cmap=plt.cm.Blues, s=5)

#Define e personaliza titulo e eixos
plt.title('Potenciação', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Value³', fontsize=14)

#Personaliza dados dos eixos
plt.tick_params(axis='both', labelsize=10)

#Define valores mínimo e máximo dos eixos
plt.axis([1, 5000, 1, 125000000001])

plt.savefig('exercicio_15.2.png', bbox_inches='tight')