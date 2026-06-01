from backend.background import Background
from backend.Const import window_height, window_width
from backend.player import Player
#classe fabrica
class EntityFactory:

    #BACKGROUND NIVEL 1
    @staticmethod
    #criar entidade
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            #entidade imagens background level 1
            case 'Level1Bg':
                lista_bg = []

                #pega todos os background e coloca na lista
                for i in range(5):
                    #carrega as 5 imagens no começo da tela
                    lista_bg.append(Background(f'background1img{i}', (0,0)))
                    #carrega as 5 imagens no final da tela
                    lista_bg.append(Background(f'background1img{i}', (window_width,0)))

                return lista_bg
            #entidade player 1 level 1
            case 'Player1':
                return Player('Player1', (20, window_height / 2 - 60))












