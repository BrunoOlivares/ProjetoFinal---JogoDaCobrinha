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
    
    #musica do menu
    pygame.mixer.music.load('musica_menu.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(loops=-1)

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
                estado_de_jogo = TA_ROLANDO
                rolando = False
                pygame.mixer.music.stop()

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return estado_de_jogo

