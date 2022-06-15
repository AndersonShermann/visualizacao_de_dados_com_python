import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk(100000)
    rw.fill_walk()

    num_points = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, edgecolors='None', c=num_points, cmap=plt.cm.Blues, s=1)

    #Enfatiza o primeiro e ultimo ponto do percurso
    plt.scatter(0, 0, c='red', edgecolors='None', s=50)
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='None', s=50)

    #Remove os eixosy
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)

    # plt.savefig('random_walk.png', bbox_inches='tight')
    plt.show()

    keep_running = input('Gerar outro caminho?(y/n): ')
    if keep_running == 'n':
        break
