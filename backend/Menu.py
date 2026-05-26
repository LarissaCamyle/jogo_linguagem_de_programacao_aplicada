import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        #carrega imagem de fundo
        self.imagem = pygame.image.load('./imagens/Menu_background.png')
        #desenha o retangulo para colocar o background
        self.background= self.background.get_rect(left=0, top=0)

    def run (self):
        #adiciona a imagem no background
        self.window.blit(source= self.imagem, dest= self.background)

        pygame.display.flip()







