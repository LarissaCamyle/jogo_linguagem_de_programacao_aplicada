#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import abstractmethod
import pygame
from backend.entity import Entity
from backend.Const import velocidade_entidades, window_height, window_width


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        #herda da classe entity
        super().__init__(name, position)

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
            #SETA PARA CIMA
            #se pressionar a seta p cima o player vai para cima no eixo y
            #vai para cima enquanto não ultrapassar o background e sumir
            if pressed_key[pygame.K_w] and self.rect.top > 0:
                #velocidade que o player se movimenta
                #diminui a posição no eixo y (altura) 
                self.rect.centery -= velocidade_entidades[self.name]

            #SETA PARA BAIXO
            #tecla para baixo player vai para baixo sem ultrapassar o background
            if pressed_key[pygame.K_s] and self.rect.bottom < window_height:
                #aumenta a posição no eixo y (altura)
                self.rect.centery += velocidade_entidades[self.name]

            #SETA PARA ESQUERDA
            if pressed_key[pygame.K_a] and self.rect.left > 0:
                #diminuindo a posição no eixo x (largura)
                self.rect.centerx -= velocidade_entidades[self.name]

            #SETA PARA DIREITA
            if pressed_key[pygame.K_d] and self.rect.right < window_width:
                #diminuindo a posição no eixo x (largura)
                self.rect.centerx += velocidade_entidades[self.name]
        pass
