import pygame

#CORES  ========================================
white = (255,255,255)
purple = (0,0,0)



#tamanho da tela ===============================
window_width = 800
window_height = 450


lista_opcoes_menu= ('NEW GAME 1P',
            'NEW GAME 2P - COOPERATIVE',
            'NEW GAME 2P - COMPETITIVE',
            'SCORE',
            'EXIT')



velocidade_entidades = {
    'background1img0': 3,
    'background1img1': 0,
    'background1img2': 3,
    'background1img3': 4,
    'background1img4': 5,
    'Player1': 5,
    'Player2': 5,
    'Enemy1': 4,
    'Enemy2': 3,
}

#user event é o evento (evento de teclado por exemplo: KEYDOWN) criado pelo usuario 
evento_inimigo = pygame.USEREVENT + 1

#tempo q nasce os inimigos
tempo_spawn = 4000


vida_entidades = {
    'background1img0': 999,
    #imagem nao se move
    'background1img1': 999,
    'background1img2': 999,
    'background1img3': 999,
    'background1img4': 999,
    'Player1': 300,
    'Player2': 300,
    'Enemy1': 50,
    'Enemy2': 60,
}
