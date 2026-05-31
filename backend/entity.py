from abc import ABC, abstractmethod
import os
import pygame

#classe abstrata
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # CORREÇÃO: Construindo o caminho dinamicamente sem a barra inicial absoluta
        # Isso vai buscar a partir de onde o main.py foi executado
        caminho_imagem = os.path.join('backend', 'img', f'{name}.png')
        
        self.surf = pygame.image.load(caminho_imagem)
        self.rect = self.surf.get_rect(left= position[0], top= position[1])
        self.speed = 0

    #não utilizará o metodo move entao coloca o 
    @abstractmethod
    def move(self, ):
        pass
