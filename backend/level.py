import random
import sys
from backend.Const import branco, window_height, lista_opcoes_menu, evento_inimigo, tempo_spawn, evento_vitoria, tempo_de_verificacao, duracao_do_level
from backend.enemy import Enemy
from backend.entity import Entity
from backend.entityFactory import EntityFactory
from backend.entityMediator import EntityMediator
import pygame

from backend.player import Player

class Level:
    def __init__(self, window, name, game_mode, player_score : list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        #lista das entidades do level 1
        self.entity_list : list[Entity] = []
        #pega todos os arquivos do background 1 e adiciona na lista de entidades
        self.entity_list.extend(EntityFactory.get_entity(self.name+'Bg'))
        
        #cria o jogador
        player = EntityFactory.get_entity('Player1')
        #pontos player1
        player.score = player_score[0]
        #adiciona o player 1 na lista de entidades
        self.entity_list.append(player)


        #se no menu for escolhido a opção cooperativo ou competitivo adiciona o player 2 como entidade
        if game_mode in [lista_opcoes_menu[1], lista_opcoes_menu[2]]:
            #cria o jogador
            player = EntityFactory.get_entity('Player2')
            #pontos player 2
            player.score = player_score[1]
            #adiciona o player 2 na lista de entidades
            self.entity_list.append(player)

        #tempo de duracao da fase
        self.timeout = duracao_do_level

        #a cada 3 segundos gera o evento criado que faz aparecer um inimigo
        pygame.time.set_timer(evento_inimigo, tempo_spawn)

        #a cada 100 mili segundos testa para ver se o jogador venceu a fase
        pygame.time.set_timer(evento_vitoria, tempo_de_verificacao)


        

    def run(self, player_score : list[int]):
        #carregar musica
        pygame.mixer_music.load(f'./backend/musicas/{self.name}.mp3')
        pygame.mixer_music.play(-1)

        #FPS do jogo
        clock = pygame.time.Clock()
        

        while True:
            #60 FPS
            clock.tick(60)


            #percorre pela lista de entidades e chama a funcao de mover
            for entity in self.entity_list:
                #printando cada uma das imagens na tela
                self.window.blit(source= entity.surf, dest=entity.rect)
                #movimento da imagem
                entity.move()

                # se a entidade for player ou inimigo chama a funcao de tiro
                if isinstance(entity, (Player,Enemy)):
                    shoot = entity.shoot()
                    #se existir um tiro adiciona na lista de entidades
                    if shoot is not None:
                        self.entity_list.append(shoot)


                #Printa a vida dos jogadores
                if entity.name == 'Player1':
                    self.level_text(12, f'Player 1 - Health : {entity.health} | Score : {entity.score}', branco, (10, 30))
                if entity.name == 'Player2':
                    self.level_text(12, f'Player 2 - Health : {entity.health} | Score : {entity.score}', branco, (10, 55))



            #EVENTOS PYGAME
            for event in pygame.event.get():
                #fecha janela
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #evento criado, que gera um inimigo a cada 2 segundos
                if event.type == evento_inimigo:  
                    #escolhe aleatório entre inimigo 1 ou inimigo 2  
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3', 'Enemy4', 'Enemy5'))


                    #printa o inimigo gerado na tela
                    self.entity_list.append(EntityFactory.get_entity(choice))

                #vai diminuindo o tempo da variavel timeout responsavel pela duracao do jogo
                if event.type == evento_vitoria:
                    self.timeout -= tempo_de_verificacao

                    #se o tempo da partida acabou retorna true e finaliza a fase
                    if self.timeout == 0:

                        #salva os pontos dos jogadores
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score

                        return True

                player_encontrado = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        player_encontrado = True

                
                if player_encontrado == False:
                    #se nao existir nenhum jogador encerra o level retornando false
                    return False


            #printa o tempo de duração da fase
            self.level_text(12, f'{self.name} = Timeout: {self.timeout / 1000 : .1f}s', branco, (10,5))
            #printa o FPS
            self.level_text(12, f'FPS: {clock.get_fps() :.0f}', branco,(10, window_height - 35))
            #quantos personagens tem na tela
            self.level_text(12, f'Entidades: {len(self.entity_list)}', branco, (10, window_height - 20))

            #printa tudo na tela
            pygame.display.flip()

            #CHAMA FUNCOES DE VERIFICACAO *****************************************************************
            #chama o evento para verificar as colisoes com a lista das entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            #chama o evento para verificar a vida das entidades
            EntityMediator.verify_health(self.window, entity_list=self.entity_list)
        pass

    #cada texto é como uma imagem no pygame
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.Font(
            "backend/fonts/Press_Start_2P/PressStart2P-Regular.ttf",
            text_size
        )
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)







