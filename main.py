#FINALIZEI A AULA 1
import pygame
#inicializa
pygame.init()


#criar janela
window = pygame.display.set_mode(size=(800, 500))

while True:
    #lista com todos os eventos que acontecerem como abrir e fechar janela e interações
    for event in pygame.event.get():
        #se o evento de tentar fechar janela acontecer
        if event.type == pygame.QUIT:
            #fecha a janela
            pygame.quit()
            #encerra o código
            quit()
           






