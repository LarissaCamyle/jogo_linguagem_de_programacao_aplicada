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

            if game_mode == lista_opcoes_menu[0]:
                #salva o score do jogador 1
                score = player_score[0]
                text = "Player 1 enter your name (10 characters)"

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

