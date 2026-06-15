import pygame

#CORES  ========================================
branco = (255,255,255)
roxo = (144, 110, 255)



#tamanho da tela ===============================
window_width = 800
window_height = 450


lista_opcoes_menu= ('NEW GAME 1 PLAYER',
            'NEW GAME 2 PLAYERS',
            'SCORE',
            'EXIT')



velocidade_entidades = {
    'background1img0': 3,
    'background1img1': 0,
    'background1img2': 3,
    'background1img3': 4,
    'background1img4': 5,
    'background2img0': 3,
    'background2img1': 0,
    'background2img2': 3,
    'background2img3': 4,
    'background2img4': 5,
    'Player1': 5,
    'Player2': 5,
    'Player1Shoot': 5,
    'Player2Shoot': 5,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy4': 1,
    'Enemy5': 1,
    'Enemy1Shoot': 3,
    'Enemy2Shoot': 3,
    'Enemy3Shoot': 3,
    'Enemy4Shoot': 3,
    'Enemy5Shoot': 3,
}

#user event é o evento (evento de teclado por exemplo: KEYDOWN) criado pelo usuario 
evento_inimigo = pygame.USEREVENT + 1

evento_vitoria= pygame.USEREVENT + 2

#tempo q nasce os inimigos
tempo_spawn = 2000

#tempo de verificacao para saber quando o jogador venceu a fase
tempo_de_verificacao = 100

#duracao do level em 20 segundos
duracao_do_level = 20000



vida_entidades = {
    'background1img0': 999,
    'background1img1': 999,
    'background1img2': 999,
    'background1img3': 999,
    'background1img4': 999,
    'background2img0': 999,
    'background2img1': 999,
    'background2img2': 999,
    'background2img3': 999,
    'background2img4': 999,
    'Player1': 300,
    'Player2': 300,
    'Player1Shoot': 1,
    'Player2Shoot': 1,
    'Enemy1': 50,
    'Enemy2': 60,
    'Enemy3': 60,
    'Enemy4': 60,
    'Enemy5': 60,
    'Enemy1Shoot': 5,
    'Enemy2Shoot': 2,
    'Enemy3Shoot': 2,
    'Enemy4Shoot': 2,
    'Enemy5Shoot': 2,
}

#delay quando aperta na tecla de atirar
tiro_delay = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 150,
    'Enemy3': 150,
    'Enemy4': 150,
    'Enemy5': 150,
}

entidade_dano = {
    'background1img0': 0,
    'background1img1': 0,
    'background1img2': 0,
    'background1img3': 0,
    'background1img4': 0,
    'background2img0': 0,
    'background2img1': 0,
    'background2img2': 0,
    'background2img3': 0,
    'background2img4': 0,
    'Player1': 1,
    'Player2': 1,
    'Player1Shoot': 25,
    'Player2Shoot': 25,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3': 1,
    'Enemy4': 1,
    'Enemy5': 1,
    'Enemy1Shoot': 20,
    'Enemy2Shoot': 15,
    'Enemy3Shoot': 15,
    'Enemy4Shoot': 15,
    'Enemy5Shoot': 15,
}

#os pontos que os jogadores recebem de acordo com cada inimigo morto
score_entidades = {
    'background1img0': 0,
    'background1img1': 0,
    'background1img2': 0,
    'background1img3': 0,
    'background1img4': 0,
    'background2img0': 0,
    'background2img1': 0,
    'background2img2': 0,
    'background2img3': 0,
    'background2img4': 0,
    'Player1': 0,
    'Player2': 0,
    'Player1Shoot': 0,
    'Player2Shoot': 0,
    'Enemy1': 100,
    'Enemy2': 125,
    'Enemy3': 125,
    'Enemy4': 100,
    'Enemy5': 100,
    'Enemy1Shoot': 0,
    'Enemy2Shoot': 0,
    'Enemy3Shoot': 0,
    'Enemy4Shoot': 0,
    'Enemy5Shoot': 0,
}

estilo_texto = {
    'Title': (window_width / 2, 80),
    'EnterName': (window_width / 2, 150),
    'Label': (window_width / 2, 180),
    'Name': (window_width / 2, 200),
    0: (window_width / 2, 170),
    1: (window_width / 2, 190),
    2: (window_width / 2, 210),
    3: (window_width / 2, 230),
    4: (window_width / 2, 250),
    5: (window_width / 2, 270),
    6: (window_width / 2, 290),
    7: (window_width / 2, 310),
    8: (window_width / 2, 330),
    9: (window_width / 2, 350),
}
