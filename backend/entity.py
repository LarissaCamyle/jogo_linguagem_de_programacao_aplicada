from abc import ABC, abstractmethod
from backend.Const import vida_entidades, entidade_dano, score_entidades
import os
from backend.CaminhoImagem import resource_path
import pygame

#classe abstrata
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Construindo o caminho dinamicamente 
        caminho_imagem = resource_path(f'assets/{name}.png')
        self.surf = pygame.image.load(caminho_imagem)
        
        #imagem
        self.rect = self.surf.get_rect(left= position[0], top= position[1])
        self.speed = 0
        #vida da entidade
        self.health = vida_entidades[self.name]
        #quantidade de dano
        self.damage = entidade_dano[self.name]
        #recebe o nome de quem matou o inimigo,para depois poder pontuar o jogador com os inimigos que o jogador matou mortos
        self.last_damage = 'None'
        #recebe o score de pontos
        self.score = score_entidades[self.name]

    #não utilizará o metodo move entao coloca o 
    @abstractmethod
    def move(self, ):
        pass
