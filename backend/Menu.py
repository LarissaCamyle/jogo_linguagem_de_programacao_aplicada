import os
from tkinter.font import Font
from backend.Const import window_height, window_width, branco, lista_opcoes_menu, roxo
import pygame

class Menu:
    def __init__(self, window):
        self.window = window
        #carrega imagem de fundo
        BASE_DIR = os.path.dirname(__file__)
        caminho_imagem = os.path.join(BASE_DIR, 'assets', 'Menu_background.png')
        self.imagem = pygame.image.load(caminho_imagem)

        #desenha o retangulo para colocar o background
        self.background= self.imagem.get_rect(left=0, top=0)

    def run (self):
        #limpa eventos antigos para não travar
        pygame.event.clear()  

        #VARIAVEIS =====================================================================================================
        #conta o for para o texto do menu selecionado
        contador_opcoes_menu = 0
        #carrega a musica
        BASE_DIR = os.path.dirname(__file__)
        caminho_musica = os.path.join(BASE_DIR, 'assets', 'menu.mp3')
        pygame.mixer_music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.3)
        #toca a musica em loop infinito
        pygame.mixer_music.play(-1)


        #INCIALIZACAO DO JOGO ===========================================================================================
        while True:

            #IMAGENS E TEXTOS DA TELA ***********************************************************************************
            #adiciona a imagem no background
            self.window.blit(source= self.imagem, dest= self.background)
            #printa os textos do menu
            for i in range (len(lista_opcoes_menu)):
                #se a linha/opcão estiver selecionado o texto fica roxo
                if i == contador_opcoes_menu:
                    self.menu_text(20, lista_opcoes_menu[i], roxo, ((window_width / 2), 300 + 40 * i))
                #se a linha/opcão não estiver selecionado o texto fica branco
                else:
                    self.menu_text(18, lista_opcoes_menu[i], branco, ((window_width / 2), 300 + 40 * i))


            #atualiza a tela para printar a imagem selecionada como imagem de fundo
            pygame.display.flip()

            #EVENTOS DE INTERAÇÃO COM O JOGO*********************************************************************************
            #lista com todos os eventos que acontecerem como o jogo
            for event in pygame.event.get():

                #se o evento de tentar fechar janela acontecer
                if event.type == pygame.QUIT:
                    #fecha a janela
                    pygame.quit()
                    #encerra o código
                    quit()

                #quando aperta tecla
                if event.type == pygame.KEYDOWN:

                    #SETA PARA CIMA
                    if event.key == pygame.K_DOWN:
                        #se o contador não chegou na última opcao 
                        if contador_opcoes_menu < len(lista_opcoes_menu) - 1:
                            contador_opcoes_menu += 1
                        #contador chegou na última opção, logo o contador é reiniciado
                        else:
                            contador_opcoes_menu = 0

                    #SETA PARA BAIXO
                    if event.key == pygame.K_UP:
                        #se o contador não chegou na primeira opção
                        if contador_opcoes_menu > 0:
                            contador_opcoes_menu -= 1
                        #contador chegou na primeira opção, logo o contador é reiniciado e colocado na opção maior do menu
                        else:
                            contador_opcoes_menu = len(lista_opcoes_menu) - 1

                    #ENTER 
                    if event.key == pygame.K_RETURN:
                        #se aperta enter finaliza a classe e retorna a opção do menu selecionada
                        return lista_opcoes_menu[contador_opcoes_menu]

    #cada texto é como uma imagem no pygame
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        BASE_DIR = os.path.dirname(__file__)
        font_path = os.path.join(BASE_DIR, 'assets', 'PressStart2P-Regular.ttf')

        text_font = pygame.font.Font(font_path, text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)









