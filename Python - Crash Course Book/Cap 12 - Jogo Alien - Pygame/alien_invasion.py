import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Começa o jogo e cria um objeto na tela
    pygame.init()

    # Importa as settings do jogo
    ai_settings = Settings()

    # Setar o tamanho da tela
    # Screen é chamado de superficie
    # Uma superfície é uma parte da tela em que exibimos os elementos do jogo
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Cria a espaçonave
    ship = Ship(screen)

    # Mostrar no display
    pygame.display.set_caption('Invasão Alien')

    # Laço principal do jogo
    while True:

        # Eventos do teclado e mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)

        ship.blitme()

        # Deixa a tela mais recente visível
        pygame.display.flip()

run_game()