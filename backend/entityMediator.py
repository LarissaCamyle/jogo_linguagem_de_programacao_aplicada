from backend.PlayerShoot import PlayerShoot
from backend.enemy import Enemy
from backend.entity import Entity
from backend.Const import window_width
from backend.EnemyShoot import EnemyShoot

class EntityMediator:

    @staticmethod
    #verifica se a entidade saiu da tela
    # os dois __ indica que o metodo só pode ser usado internamente e nao pode invocar fora da classe
    def __verify_collision_window(ent: Entity):
        #verifica a entidade para saber se ela é de inimigo e 
        #para saber se ela vai ultrapassar a tela para remover ela
        if isinstance(ent, Enemy):
            # se ultrapassar a tela e sumir deixa a vida em 0 da entidade
            if ent.rect.right < 0 :
                ent.health = 0

        #se a entidade for do tipo player shoot 
        if isinstance(ent, PlayerShoot):
            #se o tiro ultrapassar a tela do lado direito ele zera a vida
            if ent.rect.left >= window_width:
                ent.health = 0

        #se a entidade for do tipo enemy shoot 
        if isinstance(ent, EnemyShoot):
            #se o tiro ultrapassar a tela do lado esquerdo ele zera a vida
            if ent.rect.left <= 0:
                ent.health = 0
        pass



    @staticmethod
    #verifica as colisoes 
    #                   lista de entidades
    def verify_collision(entity_list : list[Entity]):
        #for em todas as entidades
        for i in range(len(entity_list)):
            entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity)
            


    @staticmethod
    #remove a entidade
    def verify_health(entity_list: list[Entity]):
        #verifica todas as entidades
        for ent in entity_list:
            #se a vida for igual ou menor que 0 remove a entidade da lista
            if ent.health <= 0:
                entity_list.remove(ent)












