import pygame


class Score:
    def __init__(self, window):
        self.window = window
        #carrega imagem de fundo
        self.imagem = pygame.image.load('./backend/img/Score.png').convert_alpha()
        #desenha o retangulo para colocar o background
        self.background= self.imagem.get_rect(left=0, top=0)

    def save_score(self):
        pass


    def show_score(self):
        pass





