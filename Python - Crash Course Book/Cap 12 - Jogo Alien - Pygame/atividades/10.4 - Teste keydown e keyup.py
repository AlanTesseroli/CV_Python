import sys
import pygame
def jogo():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (173, 216, 230)

    tecla_acionada = (100,100,100)
    tecla_solta = (173, 216, 230)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    bg_color = tecla_acionada
                if event.key == pygame.K_LEFT:
                    bg_color = tecla_acionada
                if event.key == pygame.K_UP:
                    bg_color = tecla_acionada
                if event.key == pygame.K_DOWN:
                    bg_color = tecla_acionada

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    bg_color = tecla_solta
                if event.key == pygame.K_LEFT:
                    bg_color = tecla_solta
                if event.key == pygame.K_UP:
                    bg_color = tecla_solta
                if event.key == pygame.K_DOWN:
                    bg_color = tecla_solta

        screen.fill(bg_color)
        pygame.display.flip()

jogo()
