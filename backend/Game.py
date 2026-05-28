import pygame
from backend.Menu import Menu
from backend.Const import window_width, window_height, lista_opcoes_menu

class Game:
    def __init__(self):
        #inicializa o pygame e a janela
        pygame.init()
        self.window = pygame.display.set_mode(size=(window_width, window_height))

    def run (self):
        while True:  

            #Inicializa o menu
            menu = Menu(self.window)
            menu_return = menu.run()

            #opcao iniciar jogo
            if menu_return == lista_opcoes_menu[0]:
                pass
            #opcao sair do jogo
            if menu_return == lista_opcoes_menu[4]:
                pygame.quit()
                quit()



            





