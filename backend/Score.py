import sys

import pygame
from backend.Const import branco, estilo_texto, lista_opcoes_menu
from backend.DBProxy import DBProxy

class Score:
    def __init__(self, window):
        self.window = window
        #carrega imagem de fundo
        self.imagem = pygame.image.load('./backend/img/Score.png').convert_alpha()
        #desenha o retangulo para colocar o background
        self.background= self.imagem.get_rect(left=0, top=0)

    def save_score(self, game_mode, player_score: list[int]):
        #carrega a musica
        pygame.mixer_music.load('./backend/musicas/score.mp3')
        pygame.mixer.music.set_volume(0.3)
        #toca a musica em loop infinito
        pygame.mixer_music.play(-1)

        #INICIALIZA O BANCO DE DADOS =======================================================================
        #                  nome do banco de dados
        db_proxy = DBProxy('DBScore')

        #imagem
        self.window.blit(source= self.imagem, dest=self.background)

        while True:
            self.score_text(48, "YOU WIN!!", branco, estilo_texto['Title'] )
            

            #um jogador
            if game_mode == lista_opcoes_menu[0]:
                #salva o score do jogador 1
                score = player_score[0]
                texto_pontuacao = f"PONTOS : {player_score[0]}"
                texto_nome = " Player 1 enter your name (10 characters)"

            #dois jogadores
            if game_mode == lista_opcoes_menu[1]:
                #salva o score do jogador que estiver com mais pontos
                if player_score[0] >= player_score[1]:
                    player_score[0]
                    texto_pontuacao = f"PONTOS : {player_score[0]}"
                    texto_nome = "Player 1 enter your name (10 characters)"
                else:
                    player_score[1]
                    texto_pontuacao = f"PONTOS : {player_score[1]}" 
                    texto_nome = "Player 2 enter your name (10 characters)"

            self.score_text(26, texto_pontuacao, branco, estilo_texto['EnterName'] )
            self.score_text(20, texto_nome, branco, estilo_texto['Label'] )



            #btn de fechar janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            pass


    def show_score(self):
        #carrega a musica
        pygame.mixer_music.load('./backend/musicas/score.mp3')
        pygame.mixer.music.set_volume(0.3)
        #toca a musica em loop infinito
        pygame.mixer_music.play(-1)

        #imagem
        self.window.blit(source= self.imagem, dest=self.background)

        while True:
            
            pygame.display.flip()
            pass



    #cada texto é como uma imagem no pygame
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

