from backend.background import Background
from backend.Const import window_height, window_width
#classe fabrica
class EntityFactory:

    #printa imagens na tela
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []

                #pega todos os background e coloca na lista
                for i in range(7):
                    #carrega as 7 imagens no começo da tela
                    lista_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    #carrega as 7 imagens no final da tela
                    lista_bg.append(Background(f'Level1Bg{i}', (window_width,0)))

                return lista_bg













