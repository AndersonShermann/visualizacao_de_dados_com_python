from random import choice

class RandomWalk():
    """Uma classe que gera passeios aleatórios"""
    def __init__(self, num_points=5000):
        """Método que inicializa os atributos do passeio"""
        self.num_points = num_points
        """Todos os passeios começam em (0, 0)"""
        self.x_value = [0]
        self.y_value = [0]
    
    def fill_walk(self):
        """Método que define a direção e a distância do movimento"""
        
        #Laço para contar self.num_points
        while len(self.x_value) < self.num_points:
            #Define nova direção a ser seguida e a distancia a ser percorrida
            x_direction = choice([-3, 3])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
            x_step = x_direction * x_distance

            y_direction = choice([-3, 3])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
            y_step = y_direction * y_distance

            #Rejeita movimentos que não vão a lugar nenhum
            if x_step == 0 and y_step == 0:
                continue

            #Calcula próximos valores de x e y
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)