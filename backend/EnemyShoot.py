from backend.entity import Entity
from backend.Const import velocidade_entidades


class EnemyShoot(Entity):
    def __init__(self, name: str, position: tuple):
        #herda da classe entity
        super().__init__(name, position)
        

    def move(self, ):
        #tiro do jogador vai reto da direita para esquerda no eixo x
        self.rect.centerx -= velocidade_entidades[self.name]





