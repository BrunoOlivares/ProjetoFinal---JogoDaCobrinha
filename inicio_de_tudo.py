import pygame
import random
from Game_over import game_over_sreen
from Predefinições import GAME_OVER, LARGURA, COMPRIMENTO, TA_COMEÇANDO, TA_ROLANDO, ACABOU
from Tela_Inicial import init_screen
from Tela_principal import o_jogo

pygame.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((COMPRIMENTO, LARGURA))
pygame.display.set_caption('1,2,3 BERTO')

state = TA_COMEÇANDO
while state != ACABOU:
    if state == TA_COMEÇANDO:
        state = init_screen(tela)
    elif state == TA_ROLANDO:
        state = o_jogo(tela)
    elif state == GAME_OVER:
        state = game_over_sreen(tela)
    else:
        state = ACABOU

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados