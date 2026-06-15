from backend.PlayerShoot import PlayerShoot
from backend.enemy import Enemy
from backend.entity import Entity
from backend.Const import window_width
from backend.EnemyShoot import EnemyShoot
from backend.player import Player
from backend.GameOver import GameOver

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
    #da pontos para os jogadores que mataram o inimigo
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        #se quem matou o inimigo foi o player 1
        if enemy.last_damage == "Player1Shoot":
            #Encontra o jogador 1
            for ent in entity_list:
                if ent.name == 'Player1':
                    #o jogador 1 ganha pontos referente ao inimigo que foi eliminado
                    ent.score += enemy.score
        #se quem matou o inimigo foi o player 2
        elif enemy.last_damage == "Player2Shoot":
            #Encontra o jogador 2
            for ent in entity_list:
                if ent.name == 'Player2':
                    #o jogador 2 ganha pontos referente ao inimigo que foi eliminado
                    ent.score += enemy.score


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

        #se aconteceu uma colisao valida
        #se as imagens colidiram/estao dentro uma da outra ou ocupando o mesmo espaço
        if valid_collision == True:
            #se todas as especificacoes forem true aconteceu uma colisao --------------------------------
                #1.se a borda da direita da img da ent1 estiver á direita da borda esquerda da img da ent2                                   
            if (entity1.rect.right >= entity2.rect.left and
                #2.se a borda da esquerda ent1 estiver á esquerda da borda da direita da img da ent2 
                entity1.rect.left <= entity2.rect.right and
                #3. se a borda de baixo da img ent1 estiver abaixo da borda de cima da img da ent2
                entity1.rect.bottom >= entity2.rect.top and
                #4. se a borda de cima da img ent1 estiver acima da borda inferior da img da ent2
                entity1.rect.top <= entity2.rect.bottom):
                
                #diminui a vida da entidade um de acordo com o dano q a entidade 2 causa
                entity1.health -= entity2.damage
                entity2.health -= entity1.damage

                #recebe quem deu o ultimo dano
                entity1.last_damage = entity2.name
                entity2.last_damage = entity1.name




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
    def verify_health(window, entity_list: list[Entity]):
        #verifica todas as entidades
        for ent in entity_list:
            #se a vida for igual ou menor que 0 remove a entidade da lista
            if ent.health <= 0:
                #se quem morreu foi um inimigo chama a entidade p dar pontos p quem matou o inimigo
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                #remove a entidade do jogo

                if isinstance(ent, Player):
                    #Inicializa o menu
                    GameOver = GameOver(self, window)
                    retorno = GameOver.run(self)
                entity_list.remove(ent)












