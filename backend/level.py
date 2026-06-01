import sys

from backend.entity import Entity
from backend.entityFactory import EntityFactory
import pygame

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list : list[Entity] = []
        #pega todos os arquivos do background 1
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.timeout = 20000 

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
            pygame.display.flip()

            #fecha janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            #printa texto
            self.level_text()
        pass

    #cada texto é como uma imagem no pygame
    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)







