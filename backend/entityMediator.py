from backend.PlayerShoot import PlayerShoot
from backend.enemy import Enemy
from backend.entity import Entity
from backend.Const import window_width
from backend.EnemyShoot import EnemyShoot
from backend.player import Player

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
    #verifica as colisoes validas entre entidades
    def __verify_collision_entity(entity1, entity2):
        valid_collision = False
        #se for uma entidade de inimigo e a outra um tiro do jogador --------------------
        if isinstance(entity1, Enemy) and isinstance(entity2, PlayerShoot):
            valid_collision = True
        elif isinstance(entity1, PlayerShoot) and isinstance(entity2, Enemy):
            valid_collision = True

        #se for uma entidade de tiro do inimigo e a outra do jogador --------------------
        elif isinstance(entity1, Player) and isinstance(entity2, EnemyShoot):
            valid_collision = True
        elif isinstance(entity1, EnemyShoot) and isinstance(entity2, Player):
            valid_collision = True

        pass


    @staticmethod
    #verifica as colisoes 
    #                   lista de entidades
    def verify_collision(entity_list : list[Entity]):
        #for em todas as entidades
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            #verifica se a entidade esta na janela do jogo
            EntityMediator.__verify_collision_window(entity1)

            #compara a entidade atual do for acima com todas as outras entidades
            #esse i+1 faz com que evite comparacoes duplicadas como comparar player1 com player1 e etc
            for j in range(i+1, len(entity_list)):

                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)


            


    @staticmethod
    #remove a entidade
    def verify_health(entity_list: list[Entity]):
        #verifica todas as entidades
        for ent in entity_list:
            #se a vida for igual ou menor que 0 remove a entidade da lista
            if ent.health <= 0:
                entity_list.remove(ent)












