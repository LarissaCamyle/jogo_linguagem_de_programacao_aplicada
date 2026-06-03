from backend.entity import Entity


class EntityMediator:

    @staticmethod
    #verifica se a entidade saiu da tela
    # os dois __ indica que o metodo só pode ser usado internamente e nao pode invocar fora da classe
    def __verify_collision_window():
        pass



    @staticmethod
    #verifica as colisoes 
    #                   lista de entidades
    def verify_collision(entity_list : list[Entity]):
        #for em todas as entidades
        for i in range(len(entity_list)):
            entity = entity_list[i]
            EntityMediator.__verify_collision_window(entity)
            










