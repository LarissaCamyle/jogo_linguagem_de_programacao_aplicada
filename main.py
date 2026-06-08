#AULA PRATICA 8 07:00
from backend.Game import Game
#inicializa

#inicializa o jogo
game = Game()
game.run()



"""
    *GAME :
        **Inicializa o menu
        **Entra em jogo de um player ou de 2 players
        **Soma Score das fases anteriores com novas fases
        **Muda de level
        -Seleciona o tamanho da janela do jogo

    *ENTITY :
        **Criação de entidades como background e personagens
        -Nome 
        -Caminho da imagem e printa a imagem
        -Posição da imagem
        -Velocidade
        -Vida
        -Dano
        -Quem deu o último dano
        -Score de pontos

    *ENTITY FACTORY :
        **Cria todas as entidades e passa as informações de criação como caminho da imagem, 
        posição e nome

    *ENTITY MEDIATOR :
        **Verifica se o inimigo saiu da tela para remover ele da lista e do jogo
        **Da pontos para o jogador de acordo com os inimigos mortos
        **Valida se teve uma colisão entre player e tiro ou inimigo e tiro, remove 
        a vida de acordo com o dano causado
        **Remove do jogo se a entidade estiver sem vida, e se for um inimigo quem morreu
        o jogador que matou ganha pontos
    
    MENU : 
        **Printa o menu com música
        **Printa as opções de menu
        **Função de selecionar uma opção no menu com o teclado
        -Imagem do menu
        -Música do menu

    LEVEL : 
        **Verifica se o level acabou para iniciar um novo 
        **Printa o background do level e a musica
        **Seleciona o FPS (Velocidade do jogo)
        **Adiciona o tiro a cada inimigo no intervalo de tempo escolhido
        **Printa a vida e os pontos dos jogadores
        **Se o player não existir mais o level finaliza
        **Chama as funcoes do entity mediator
        -Janela
        -Nome do level
        -Tipo de jogo (1 player ou 2 players)
        -Lista de entidades do level
        -Lista de todos os backgrounds do Level 1
        -Adiciona a quantidade de Players de acordo com o escolhido
        -Duração do level
        -Evento loop para aparecer inimigos de acordo com o intervalo escolhido
        
        
    PLAYER : 
        **Movimentação dos players 
        **Tiros dos players com delay
        -Herda os atributos da entity

    PLAYER SHOOT :
        **Velocidade e movimento do tiro
        -Herda os atributos da entity

    BACKGROUND :
        **Movimentação do background com o paralaxe
        -Herda os atributos da entity

    ENEMY :
        **Movimentação do inimigo
        **Tiro do inimigo
        -Herda os atributos da entity

    ENEMY SHOOT :
        **Velocidade e movimento do tiro
        -Herda os atributos da entity

    CONST : 
        -Cores
        -Tamanho das telas
        -Opcoes de menu
        -Velocidade das entidades
        -Tempo de spawn dos inimigos
        -Tempo de verificação para saber se ganhou a partida
        -Duração do nível
        -Vida das entidades
        -Delay do tiro
        -Entidade dano
        -Score entidades

"""   


