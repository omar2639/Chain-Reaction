import pygame
import sys

pygame.init()


COMPRIMENTO = 600
LARGURA = 400

pantalla = pygame.display.set_mode((COMPRIMENTO,LARGURA))

pygame.display.set_caption("Primeira Tela criada")

relogio = pygame.time.Clock()

executando = True

while executando:
    #Agora esta parte é muito importante temos que ter os eventos que acontecen
    #ao longo da execução do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False


    #Atualiza a tela para repintar-a
    pygame.display.flip()

    #Manten os FPS estaveis
    relogio.tick(60)


pygame.quit()
sys.exit()

print("Hello World!!!!")