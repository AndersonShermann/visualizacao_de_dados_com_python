#Cubos: Um número elevado a terceira potencia é chamado de cubo. Faça a plotagem dos cinco primeiro números elevados ao cubo e,
# em seguida, dos primeiros 5.000 números elevados ao cubo.
import matplotlib.pyplot as plt

x_value = list(range(1, 6))
y_value = [x**3 for x in x_value]

x2_value = list(range(1, 5001))
y2_value = [x2**3 for x2 in x2_value]

#Plota e estiliza x_value e y_value
plt.plot(x_value, y_value, c='Red', linewidth=3)

#Plota e estiliza x2_value e y2_value
plt.scatter(x2_value, y2_value, edgecolors='None', c='Blue', s=5)

#Define e estiliza titulo e eixos
plt.title('Potenciação', fontsize=24)
plt.xlabel('Valor', fontsize=14)
plt.ylabel('Valor³', fontsize=14)

#Estiliza dado dos eixos
plt.tick_params(axis='both', labelsize=10)

#Define valores mínimo e máximo dos eixos
plt.axis([1, 5001, 1, 125000000001])

plt.savefig('exercicio_15.1.png', bbox_inches='tight')