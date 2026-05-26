import pygame
from backend.Menu import Menu

class Game:
    def __init__(self):
        #inicializa o pygame e a janela
        pygame.init()
        self.window = pygame.display.set_mode(size=(800, 500))

    def run (self):
        while True:
            # #lista com todos os eventos que acontecerem como abrir e fechar janela e interações
            # for event in pygame.event.get():
            #     #se o evento de tentar fechar janela acontecer
            #     if event.type == pygame.QUIT:
            #         #fecha a janela
            #         pygame.quit()
            #         #encerra o código
            #         quit()
            

            #Inicializa o menu
            menu = Menu(self.window)
            menu.run()
            pass






