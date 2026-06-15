from tkinter.font import Font
from backend.Const import window_height, window_width, branco, lista_opcoes_menu, roxo
from backend.Menu import Menu

import pygame

class GameOver:
    def __init__(self, window):
        self.window = window
        #carrega imagem de fundo
        self.imagem = pygame.image.load('./backend/img/GameOver.png').convert_alpha()
        #desenha o retangulo para colocar o background
        self.background= self.imagem.get_rect(left=0, top=0)

    def run (self):
        #VARIAVEIS =====================================================================================================
        #conta o for para o texto do menu selecionado
        contador_opcoes_menu = 0
        #carrega a musica
        pygame.mixer_music.load('./backend/musicas/GameOver.mp3')
        pygame.mixer.music.set_volume(0.3)
        #toca a musica em loop infinito
        pygame.mixer_music.play(-1)


        #INCIALIZACAO DO JOGO ===========================================================================================
        while True:

            #IMAGENS E TEXTOS DA TELA ***********************************************************************************

            #adiciona a imagem no background
            self.window.blit(source= self.imagem, dest= self.background)

            #printa os textos do menu
            self.gameover_text(20, "Enter to Continue", branco, ((window_width / 2), 300))

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

                    #ENTER 
                    if event.key == pygame.K_RETURN:
                        #se apertar o enter inicializa o menu
                        menu = Menu(self.window)
                        menu_return = menu.run()



    #cada texto é como uma imagem no pygame
    def gameover_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.Font(
            "backend/fonts/Press_Start_2P/PressStart2P-Regular.ttf",
            text_size
        )
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)









