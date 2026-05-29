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

    def run(self):
        while True:
            #printando cada uma das imagens na tela
            for background in self.entity_list:
                self.window.blit(source= background.surf, dest=background.rect)
                #movimento da imagem
                background.move()
            pygame.display.flip()
        pass









