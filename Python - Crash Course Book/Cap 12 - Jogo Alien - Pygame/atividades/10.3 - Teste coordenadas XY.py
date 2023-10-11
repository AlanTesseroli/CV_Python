import sys
import pygame
def jogo():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    bg_color = (173, 216, 230)
    image = pygame.image.load('boneco.bmp')
    rect = image.get_rect()
    screen_rect = screen.get_rect()

    rect.centerx = screen_rect.centerx
    rect.centery = screen_rect.centery
    rect.bottom = screen_rect.bottom

    moving_right = False
    moving_left = False
    moving_up = False
    moving_down = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                if event.key == pygame.K_LEFT:
                    moving_left = True
                if event.key == pygame.K_UP:
                    moving_up = True
                if event.key == pygame.K_DOWN:
                    moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                if event.key == pygame.K_LEFT:
                    moving_left = False
                if event.key == pygame.K_UP:
                    moving_up = False
                if event.key == pygame.K_DOWN:
                    moving_down = False

        if moving_right and rect.right < screen_rect.right:
            rect.centerx += 2  # Ajuste a velocidade de movimento conforme necessário
        if moving_left and rect.left > 0:
            rect.centerx -= 2  # Ajuste a velocidade de movimento conforme necessário
        if moving_up and rect.top > 0:
            rect.centery -= 2  # Ajuste a velocidade de movimento conforme necessário
        if moving_down and rect.bottom < screen_rect.bottom:
            rect.centery += 2  # Ajuste a velocidade de movimento conforme necessário

        screen.fill(bg_color)
        screen.blit(image, rect)
        pygame.display.flip()

jogo()
