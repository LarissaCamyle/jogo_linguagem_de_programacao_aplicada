import pygame
from backend.Menu import Menu
from backend.Score import Score
from backend.Const import window_width, window_height, lista_opcoes_menu
from backend.level import Level
from backend.GameOver import GameOver

class Game:
    def __init__(self):
        #inicializa o pygame e a janela
        pygame.init()
        self.window = pygame.display.set_mode(size=(window_width, window_height))

    def run (self):
        while True:  
            score = Score(self.window)

            #limpa eventos antigos para não travar
            pygame.event.clear()  

            #Inicializa o menu
            menu = Menu(self.window)
            menu_return = menu.run()

            #OPCAO DE INICIAR JOGO ===============================================
            if menu_return in [lista_opcoes_menu[0], lista_opcoes_menu[1]]:
                #inicializa o score dos player em 0
                #[Player1, Player2]
                player_score = [0, 0]

                #inicia o level 1, se o return for true significa que nenhum jogador morreu,
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                #se vencer o level 1 vai para o level 2
                if level_return == True:
                    level2 = Level(self.window, 'Level2', menu_return, player_score)
                    level2_return = level2.run(player_score)

                    #salva o score dos jogadores
                    score.save_score(menu_return, player_score)

                    #se morreu no level 2 abre a tela do game over
                    if level2_return == False:
                        game_over = GameOver(self.window)
                        game_over.run()
                #se morreu no level 1 abre a tela de game over
                else:
                    game_over = GameOver(self.window)
                    game_over.run()


            #OPCAO DE MOSTRAR TOP 10 SCORE ==========================================
            if menu_return == lista_opcoes_menu[2]:
                score.show_score()

            #OPCAO DE FECHAR O JOGO =================================================
            if menu_return == lista_opcoes_menu[3]:
                pygame.quit()
                quit()
                return



