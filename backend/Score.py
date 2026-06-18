import datetime
import os
import sys
from datetime import datetime
import pygame
from backend.Const import branco, estilo_texto, lista_opcoes_menu, estilo_texto_tabela, window_width
from backend.CaminhoImagem import resource_path
from backend.DBProxy import DBProxy

class Score:
    def __init__(self, window):
        self.window = window
        #carrega imagem de fundo
        caminho_imagem = resource_path('assets/Score.png')

        self.imagem = pygame.image.load(caminho_imagem)
        #desenha o retangulo para colocar o background
        self.background= self.imagem.get_rect(left=0, top=0)

    def save_score(self, game_mode, player_score: list[int]):
        #carrega a musica
        caminho_musica = resource_path('assets/Score.mp3')
        pygame.mixer_music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.3)
        #toca a musica em loop infinito
        pygame.mixer_music.play(-1)

        #INICIALIZA O BANCO DE DADOS =======================================================================
        #                  nome do banco de dados
        db_proxy = DBProxy('DBScore.db')

        #nome do jogador
        name = ''

        while True:
            #imagem
            self.window.blit(source= self.imagem, dest=self.background)
            
            self.score_text(45, "YOU WIN!", branco, estilo_texto['Title'] )

            #um jogador
            if game_mode == lista_opcoes_menu[0]:
                #salva o score do jogador 1
                score = player_score[0]
                texto_score = f"PONTOS : {player_score[0]}"
                texto_nome = f"Player 1 enter your name (10 characters)"

            #dois jogadores
            if game_mode == lista_opcoes_menu[1]:
                #salva o score do jogador que estiver com mais pontos
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    texto_score= f"PONTOS : {player_score[0]}"
                    texto_nome = f"Player 1 enter your name (10 characters)"
                else:
                    score = player_score[1]
                    texto_score= f"PONTOS : {player_score[1]}"
                    texto_nome = f"Player 2 enter your name (10 characters)"

            self.score_text(25, texto_score, branco, estilo_texto['EnterName'] )
            self.score_text(15, texto_nome, branco, estilo_texto['Name'] )


            #btn de fechar janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                

                elif event.type ==  pygame.KEYDOWN:
                    #se clicou em enter verifica se oq foi escrito antes tem 10 ou menos caracteres
                    if event.key == pygame.K_RETURN and len(name) <= 10:
                        #inserir no banco de dados
                        db_proxy.save({'self': self, 'name' : name, 'score': score, 'date': get_formatted_date()})

                        #troca a tela
                        self.show_score()

                        #volta para o menu
                        return 
                    #apagar oq foi escrito
                    elif event.key == pygame.K_BACKSPACE:
                        #apaga o ultimo caracter
                        name = name[:-1]
                    #se foi escrito uma letra ele vai armazenando na variavel nome
                    #ENTER 
                    elif event.key == pygame.K_RETURN:
                        #se apertar o enter inicializa o menu
                        self.show_score()
                    else:
                        if len(name) < 10:
                            name += event.unicode

            self.score_text(25, name, branco, estilo_texto[4] )


            pygame.display.flip()
            pass


    def show_score(self):
        #carrega a musica
        caminho_musica = resource_path('assets/Score.mp3')
        pygame.mixer_music.load(caminho_musica)
        pygame.mixer.music.set_volume(0.3)
        #toca a musica em loop infinito
        pygame.mixer_music.play(-1)

        #retorna a lista dos top 10 usuarios
        db_proxy = DBProxy('DBScore.db')
        lista_score = db_proxy.score_top10()
        db_proxy.close()

        while True:
            #imagem
            self.window.blit(source= self.imagem, dest=self.background)
            #titulo
            self.score_table(48, "TOP 10 SCORE", branco, estilo_texto_tabela['Title'] )
            #cabecalho com palavras alinhadas
            cabecalho = f"NAME       SCORE        DATE"
            self.score_table(20, cabecalho, branco, estilo_texto_tabela['Table'])

            linha = f"_________________________________"
            self.score_table(20, linha, branco, estilo_texto_tabela['Line'])
            
            self.score_text(20, "ESC to Continue", branco, ((window_width / 2), 420))

            contador = 0

            for player_score in lista_score:
                id_, name, score, date = player_score
                #linha alinhada em formato de tabela
                linha = f"{name[:10]:<10} {score:05d} {date}"

                self.score_table(
                    20,
                    linha,
                    branco,
                    estilo_texto_tabela[contador]
                )
                contador += 1



            #btn de fechar janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return

                #esc
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    
                
            pygame.display.flip()
            


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font_path = resource_path('assets/PressStart2P-Regular.ttf')

        text_font = pygame.font.Font(font_path, text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    #cada texto é como uma imagem no pygame
    def score_table(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        font_path = resource_path('assets/PressStart2P-Regular.ttf')

        text_font = pygame.font.Font(font_path, text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(topleft=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

#retorna a data
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"