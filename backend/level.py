import sys
from backend.Const import white, window_height, lista_opcoes_menu
from backend.entity import Entity
from backend.entityFactory import EntityFactory
import pygame

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        #lista das entidades do level 1
        self.entity_list : list[Entity] = []
        #pega todos os arquivos do background 1 e adiciona na lista de entidades
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        #adiciona o player 1 na lista de entidades
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000 #20 segundos

        #se no menu for escolhido a opção cooperativo ou competitivo adiciona o player 2 como entidade
        if game_mode in [lista_opcoes_menu[1], lista_opcoes_menu[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        #a cada x tempo aparece um inimig
        pygame.time.set_timer()
        

    def run(self):
        #carregar musica
        pygame.mixer_music.load(f'./backend/musicas/{self.name}.mp3')
        pygame.mixer_music.play(-1)

        #FPS do jogo
        clock = pygame.time.Clock()
        

        while True:
            #60 FPS
            clock.tick(60)
            #printando cada uma das imagens na tela

            #printa imagem
            for background in self.entity_list:
                self.window.blit(source= background.surf, dest=background.rect)
                #movimento da imagem
                background.move()


            #fecha janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            #printa o tempo de duração da fase
            self.level_text(16, f'{self.name} = Timeout: {self.timeout / 1000 : .1f}s', white, (10,5))
            #printa o FPS
            self.level_text(16, f'FPS: {clock.get_fps() :.0f}', white,(10, window_height - 35))
            #quantos personagens tem na tela
            self.level_text(16, f'Entidades: {len(self.entity_list)}', white, (10, window_height - 20))

            #printa tudo na tela
            pygame.display.flip()
        pass

    #cada texto é como uma imagem no pygame
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: pygame.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)







