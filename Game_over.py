import pygame
import random
from Predefinicoes import settings

from pygame.image import load
from assets import load_assets

def game_over_sreen(tela):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets=load_assets()
    tela_game_over=assets['bg game over']
    tela_rect_game_over=assets['bg rect game over']
    musica_game_over=assets['musica game over']

    # Carrega o fundo da tela inicial
  

    #musica
    pygame.mixer.music.load(musica_game_over)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=0)

    rolando = True
    while rolando:

        # Ajusta a velocidade do jogo.
        clock.tick(settings.fps)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.

            if event.type == pygame.QUIT:
                estado_de_jogo = settings.over
                rolando = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_c:

                    estado_de_jogo = settings.start
                    rolando = False


        # A cada loop, redesenha o fundo e os sprites
        tela.blit(tela_game_over, tela_rect_game_over)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado_de_jogo

