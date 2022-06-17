#Movimento Molecular: Modifique rw_visual.py substituindo plt.scatter() por plt.plot(). Para simular o percurso de um grão de pólen na
#superfície de uma gota d'água, passe rw.x_value e rw.y_Value e inclua um argumento linewidht. Utilize 5.000 ao invés de 50.000 pontos.
import matplotlib.pyplot as plt
import sys
sys.path.append('random_walk')
from random_walk import RandomWalk


while True:

    #Importação dos métodos
    rw = RandomWalk()
    rw.fill_walk()

    #Plotagem e estilização
    plt.plot(rw.x_value, rw.y_value, linewidth=1, c='gray')

    #Marca o inicio do random walk com um ponto azul e final com um ponto vermelho
    plt.scatter(rw.x_value[0], rw.y_value[0], c='blue', s=50)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', s=50)

    #limpeza dos eixos
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    #plt.savefig('exercício_15.3.png', bbox_inches='tight')
    plt.show()

    keep_running = input('Gostaria de gerar uma nova visualização?(y/n)')
    if keep_running == 'n':
        break