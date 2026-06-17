import random

from backend.background import Background
from backend.Const import window_height, window_width
from backend.enemy import Enemy
from backend.player import Player
#classe fabrica de todas as entidades
class EntityFactory:
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
            
            #entidade imagens background level 2
            case 'Level2Bg':
                lista_bg = []

                #pega todos os background e coloca na lista
                for i in range(5):
                    #carrega as 5 imagens no começo da tela
                    lista_bg.append(Background(f'background2img{i}', (0,0)))
                    #carrega as 5 imagens no final da tela
                    lista_bg.append(Background(f'background2img{i}', (window_width,0)))

                return lista_bg
            
            #entidade player 1 
            case 'Player1':
                return Player('Player1', (20, window_height / 2 - 60))
            
            #entidade player 2 
            case 'Player2':
                return Player('Player2', (20, window_height / 2 + 20))

            #entidade enemy 
            case 'Enemy1':
                #                       vem fora da tela   
                #                                           nasce aleatoriamente no eixo y
                #                      não nascerem muito alto ou muito baixo
                return Enemy('Enemy1', (window_width + 10, random.randint(40, window_height - 40)))
            
            case 'Enemy2':
                return Enemy('Enemy2', (window_width + 10, random.randint(40, window_height - 40)))

            case 'Enemy3':
                return Enemy('Enemy3', (window_width + 10, random.randint(40, window_height - 40)))

            case 'Enemy4':
                return Enemy('Enemy4', (window_width + 10, random.randint(40, window_height - 40)))

            case 'Enemy5':
                return Enemy('Enemy5', (window_width + 10, random.randint(40, window_height - 40)))

















