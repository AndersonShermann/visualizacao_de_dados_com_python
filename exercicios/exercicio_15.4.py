#Passeios aleatórios modificados: Na classe RandomWalk, x_step e y_step são gerados a partir do mesmo conjunto de condições. A direção é
# escolhida aleatoriamente a partir da lista [1, -1], e a distancia a partir da lista [0, 1, 2, 3, 4]. Modifique os valores dessas listas 
# para ver o que acontece com o formato geral de seus passeios. Experimente usar uma lista maior de opções para a distancia, por exemplo
# de 0 a 8, ou remova o -1 da lista de direções x ou Y.
import sys
sys.path.append('random_walk')
from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_walk()

while True:
    # Plotagem e estilização
    plt.scatter(rw.x_value, rw.y_value,c=rw.y_value, cmap=plt.cm.Blues, s=5, edgecolors='None')
    # plt.plot(rw.x_value, rw.y_value)
    
    # Limpeza de eixos
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    plt.title('Direção [-3, 3], Distancia [ 0 à 12] scatter', fontsize=10)
    
    plt.savefig('exercicio_14.4.2.png', bbox_inches='tight')
    plt.show()


    keep_running = input('Deseja gerar um novo caminho? (y / n)')
    if keep_running == 'n':
        break