#AULA PRATICA 5 16:20
from backend.Game import Game
#inicializa

#inicializa o jogo
game = Game()
game.run()



"""
    *ENTITY : responsável pela criação de entidades como background e personagens
        -Nome 
        -Caminho da imagem e printa a imagem
        -Posição da imagem
        -
    
    PLAYER : responsável pela movimentação dos players
        -Herda os atributos da entity

    BACKGROUND : responsável pela movimentação do background e pelo efeito de camadas
    de imagens com o paralaxe
        -Herda os atributos da entity




    ENTITY MEDIATOR : Remove entidades que já não aparecem mais na tela
    trata as colisoes dos jogadores com os inimigos


"""   


