import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #Cria um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_value, rw.y_value, edgecolors='None', c=rw.y_value, cmap=plt.cm.Reds, s=5)

    #Define o titulo e nome dos eixos
    plt.title('Geração e Plotagem de Valores Aleatórios', fontsize=15)
    plt.xlabel('X Value', fontsize=10)
    plt.ylabel('Y Value', fontsize=10)

    #Personaliza os dados dos eixos
    plt.tick_params(axis='both', labelsize=10)

    #Define os limites mínimo e máximo dos eixos
    plt.axis([-900, 900, -900, 900])

    # plt.savefig('random_walk.png', bbox_inches='tight')
    plt.show()

    keep_running = input('Gerar outro caminho?(y/n): ')
    if keep_running == 'n':
        break
