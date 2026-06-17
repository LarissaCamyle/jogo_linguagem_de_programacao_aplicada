from abc import abstractmethod
import pygame
from backend.PlayerShoot import PlayerShoot
from backend.entity import Entity
from backend.Const import velocidade_entidades, window_height, window_width, tiro_delay

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        #herda da classe entity
        super().__init__(name, position)
        self.tiro_delay = tiro_delay[self.name]

    def move(self):
        #tecla pressionada
        pressed_key = pygame.key.get_pressed()
        
        #PLAYER 1 MOVIMENTAÇÃO --------------------------------------------------
        if self.name == "Player1":
            #SETA PARA CIMA
            #se pressionar a seta p cima o player vai para cima no eixo y
            #vai para cima enquanto não ultrapassar o background e sumir
            if pressed_key[pygame.K_UP] and self.rect.top > 0:
                #velocidade que o player se movimenta
                #diminui a posição no eixo y (altura) 
                self.rect.centery -= velocidade_entidades[self.name]

            #SETA PARA BAIXO
            #tecla para baixo player vai para baixo sem ultrapassar o background
            if pressed_key[pygame.K_DOWN] and self.rect.bottom < window_height:
                #aumenta a posição no eixo y (altura)
                self.rect.centery += velocidade_entidades[self.name]

            #SETA PARA ESQUERDA
            if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
                #diminuindo a posição no eixo x (largura)
                self.rect.centerx -= velocidade_entidades[self.name]

            #SETA PARA DIREITA
            if pressed_key[pygame.K_RIGHT] and self.rect.right < window_width:
                #diminuindo a posição no eixo x (largura)
                self.rect.centerx += velocidade_entidades[self.name]


        #PLAYER 2 MOVIMENTACAO -----------------------------------------------------
        else:
            #TECLA W
            #se pressionar a seta p cima o player vai para cima no eixo y
            #vai para cima enquanto não ultrapassar o background e sumir
            if pressed_key[pygame.K_w] and self.rect.top > 0:
                #velocidade que o player se movimenta
                #diminui a posição no eixo y (altura) 
                self.rect.centery -= velocidade_entidades[self.name]

            #TECLA S
            #tecla para baixo player vai para baixo sem ultrapassar o background
            if pressed_key[pygame.K_s] and self.rect.bottom < window_height:
                #aumenta a posição no eixo y (altura)
                self.rect.centery += velocidade_entidades[self.name]

            #TECLA A (ESQUERDA)
            if pressed_key[pygame.K_a] and self.rect.left > 0:
                #diminuindo a posição no eixo x (largura)
                self.rect.centerx -= velocidade_entidades[self.name]

            #TECLA D (ESQUERDA)
            if pressed_key[pygame.K_d] and self.rect.right < window_width:
                #diminuindo a posição no eixo x (largura)
                self.rect.centerx += velocidade_entidades[self.name]
        pass


    def shoot(self):
        #faz um loop diminuindo o delay do shoot (100)
        #para ter um tempo de intervalo entre os tiros
        self.tiro_delay -= 1

        if self.tiro_delay == 0:
            #reseta o delay
            self.tiro_delay = tiro_delay[self.name]

            #tecla pressionada
            pressed_key = pygame.key.get_pressed()
            
            #PLAYER 1 MOVIMENTAÇÃO --------------------------------------------------
            if self.name == "Player1":
                #CTRL DA DIREITA / TIRO JOGADOR 1
                #se pressionar o ctrl da direita o tiro é disparado em linha reta no eixo x
                if pressed_key[pygame.K_RCTRL]:
                    #o tiro nasce centralizado no local onde o jogador esta no momento
                    #                                                                   posiciona o tiro saindo da vassoura
                    return PlayerShoot(name="Player1Shoot", position=(self.rect.centerx + 20,self.rect.centery + 23))

                    #PLAYER 2 MOVIMENTACAO -----------------------------------------------------
            else:
                #CTRL DA ESQUERDA / TIRO JOGADOR 2
                #se pressionar o ctrl da esquerda o tiro é disparado em linha reta no eixo x
                if pressed_key[pygame.K_LCTRL]:
                    #o tiro nasce centralizado no local onde o jogador esta no momento
                    return PlayerShoot(name="Player2Shoot", position=(self.rect.centerx + 20,self.rect.centery + 19))
