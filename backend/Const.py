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
    'Player1Shoot': 3,
    'Player2Shoot': 4,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shoot': 3,
    'Enemy2Shoot': 3,
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
    'Player1Shoot': 1,
    'Player2Shoot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy1Shoot': 5,
    'Enemy2Shoot': 2,
}

#delay quando aperta na tecla de atirar
shoot_delay = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
}


