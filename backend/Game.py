import pygame
from backend.Menu import Menu
from backend.Const import window_width, window_height

class Game:
    def __init__(self):
        #inicializa o pygame e a janela
        pygame.init()
        self.window = pygame.display.set_mode(size=(window_width, window_height))

    def run (self):
        while True:  

            #Inicializa o menu
            menu = Menu(self.window)
            menu.run()
            pass






