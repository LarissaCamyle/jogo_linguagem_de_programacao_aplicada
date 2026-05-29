from backend.background import Background
#classe fabrica
class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []

                #pega todos os background e coloca na lista
                for i in range(7):
                    lista_bg.append(Background(f'Level1Bg{i}', position))

                return lista_bg













