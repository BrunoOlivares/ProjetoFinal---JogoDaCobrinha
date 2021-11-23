import pygame
import random
from Predefinições import ACABOU, FPS, TA_ROLANDO, LARGURA, COMPRIMENTO

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('Tela_inicial_ctexto.png').convert()
    background = pygame.transform.scale(background, (COMPRIMENTO, LARGURA))
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = ACABOU
                running = False

            if event.type == pygame.KEYDOWN:
                state = TA_ROLANDO
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

