from tkinter.font import Font
from backend.Const import window_height, window_width, black

import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        #carrega imagem de fundo
        self.imagem = pygame.image.load('./backend/imagens/Menu_background.png')
        #desenha o retangulo para colocar o background
        self.background= self.imagem.get_rect(left=0, top=0)

    def run (self):
        #carrega a musica
        pygame.mixer_music.load('./backend/musicas/menu.mp3')
        pygame.mixer.music.set_volume(0.2)
        #toca a musica em loop infinito
        pygame.mixer_music.play(-1)


        while True:
            #adiciona a imagem no background
            self.window.blit(source= self.imagem, dest= self.background)

            #texto print na tela
            self.menu_text(50, "Jogo Teste",black, ((window_width / 2), 70))



            #atualiza a tela para printar a imagem
            pygame.display.flip()




            #lista com todos os eventos que acontecerem como abrir e fechar janela e interações
            for event in pygame.event.get():
                #se o evento de tentar fechar janela acontecer
                if event.type == pygame.QUIT:
                    #fecha a janela
                    pygame.quit()
                    #encerra o código
                    quit()

    #cada texto é como uma imagem no pygame
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)









