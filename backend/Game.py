import pygame
from backend.Menu import Menu
from backend.Score import Score
from backend.Const import window_width, window_height, lista_opcoes_menu
from backend.level import Level

class Game:
    def __init__(self):
        #inicializa o pygame e a janela
        pygame.init()
        self.window = pygame.display.set_mode(size=(window_width, window_height))

    def run (self):
        while True:  
            score = Score(self.window)


            #Inicializa o menu
            menu = Menu(self.window)
            menu_return = menu.run()

            #opcao iniciar jogo
            if menu_return in [lista_opcoes_menu[0], lista_opcoes_menu[1], lista_opcoes_menu[2]]:
                #[Player1, Player2]
                player_score = [0, 0]

                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)

                #se vencer o level 1 vai para o level 2
                if level_return == True:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

                    score.save_score(menu_return, player_score)


            #opção de mostrar o score
            if menu_return == lista_opcoes_menu[3]:
                score.show_score()

            #opcao sair do jogo
            if menu_return == lista_opcoes_menu[4]:
                pygame.quit()
                quit()



            





