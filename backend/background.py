#!/usr/bin/python
# -*- coding: utf-8 -*-

from backend.entity import Entity
from backend.Const import window_width, velocidade_entidades


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        #pega a velocidade com q as imagens se movem de acordo com o nome da imagem
        self.rect.centerx -= velocidade_entidades[self.name]

        #quando o final da imagem chegar no começo da tela, joga a imagem para o final novamente
        if self.rect.right <= 0:
            self.rect.left = window_width
        
