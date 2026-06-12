import datetime
import sys
from datetime import datetime
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

        #nome do jogador
        name = ''

        while True:
            #imagem
            self.window.blit(source= self.imagem, dest=self.background)

            self.score_text(48, "YOU WIN!!", branco, estilo_texto['Title'] )
            

            #um jogador
            if game_mode == lista_opcoes_menu[0]:
                #salva o score do jogador 1
                score = player_score[0]
                texto_nome = f"PONTOS : {player_score[0]}  |  Player 1 enter your name (10 characters)"

            #dois jogadores
            if game_mode == lista_opcoes_menu[1]:
                #salva o score do jogador que estiver com mais pontos
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    texto_nome = f"PONTOS : {player_score[0]}  |  Player 1 enter your name (10 characters)"
                else:
                    score = player_score[1]
                    texto_nome = f"PONTOS : {player_score[1]}  |  Player 1 enter your name (10 characters)"

            self.score_text(20, texto_nome, branco, estilo_texto['EnterName'] )



            #btn de fechar janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type ==  pygame.KEYDOWN:
                    #se clicou em enter verifica se oq foi escrito antes tem 10 ou menos caracteres
                    if event.key == pygame.K_RETURN and len(name) <= 10:
                        #inserir no banco de dados
                        db_proxy.save({'self': self, 'name' : name, 'score': score, 'date': get_formatted_date()})
                        #troca a tela
                        self.show_score()
                    #apagar oq foi escrito
                    elif event.key == pygame.K_BACKSPACE:
                        #apaga o ultimo caracter
                        name = name[:-1]
                    #se foi escrito uma letra ele vai armazenando na variavel nome
                    else:
                        if len(name) < 10:
                            name += event.unicode

            self.score_text(25, name, branco, estilo_texto['Label'] )


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

        self.score_text(48, "TOP 10 SCORE", branco, estilo_texto['Title'] )

        self.score_text(20, 'NAME           SCORE           DATE', branco, estilo_texto['Name']) 

        #retorna a lista dos top 10 usuarios
        db_proxy = DBProxy('DBScore')
        lista_score = DBProxy.score_top10()
        db_proxy.close()

        for player_score in lista_score:
            id, name, score, date = player_score
            self.score_text(20, f'{name}          {score :05d}      {date}', branco, estilo_texto[lista_score.index(player_score)])

        while True:
            #btn de fechar janela
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
            pygame.display.flip()
            



    #cada texto é como uma imagem no pygame
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

#retorna a data
def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"