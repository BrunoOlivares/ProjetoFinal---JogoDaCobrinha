import pygame
import random
from Predefinições import ACABOU, FPS, TA_ROLANDO, LARGURA, COMPRIMENTO, TA_COMEÇANDO

def game_over_sreen(tela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load('Tela_de_game_over.png').convert()
    background = pygame.transform.scale(background, (COMPRIMENTO, LARGURA))
    background_rect = background.get_rect()

    #musica
    pygame.mixer.music.load('game_over.wav')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=0)

    rolando = True
    while rolando:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.

            if event.type == pygame.QUIT:
                estado_de_jogo = ACABOU
                rolando = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:

                    estado_de_jogo = TA_COMEÇANDO
                    rolando = False


        # A cada loop, redesenha o fundo e os sprites
        tela.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado_de_jogo

