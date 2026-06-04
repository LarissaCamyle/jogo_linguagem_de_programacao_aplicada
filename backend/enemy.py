#!/usr/bin/python
# -*- coding: utf-8 -*-
from backend.Const import velocidade_entidades, window_width, shoot_delay
from backend.entity import Entity
from backend.EnemyShoot import EnemyShoot


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        #herda da classe entity
        super().__init__(name, position)
        self.shoot_delay = shoot_delay[self.name]
        

    def move(self, ):
        #pega a velocidade com q as imagens se movem de acordo com o nome da imagem
        self.rect.centerx -= velocidade_entidades[self.name]

    def shoot(self):
        #faz um loop diminuindo o delay do shoot (30)
        #para ter um tempo de intervalo entre os tiros
        self.shoot_delay -= 1

        if self.shoot_delay == 0:
            #reseta o delay
            self.shoot_delay = shoot_delay[self.name]
            #retorna o tiro na posicao do inimigo
            return EnemyShoot(name=f'{self.name}Shoot', position=(self.rect.centerx,self.rect.centery))





