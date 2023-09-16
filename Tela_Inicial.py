import pygame
import random
from assets import load_assets
from Predefinicoes import settings

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets=load_assets()
    musica_menu=assets['musica menu']
    bg_inicial=assets['bg inicial']
    bg_rect_inicial=assets['bg rect inicial']

    # Carrega o fundo da tela inicial
    
    
    #musica do menu
    pygame.mixer.music.load(musica_menu)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

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
                estado_de_jogo = settings.happening
                rolando = False
                pygame.mixer.music.stop()

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(bg_inicial, bg_rect_inicial)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado_de_jogo

