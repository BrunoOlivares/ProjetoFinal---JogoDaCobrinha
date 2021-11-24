import pygame
import random
from Predefinições import LARGURA, COMPRIMENTO, TA_COMEÇANDO, TA_ROLANDO, ACABOU
from Tela_Inicial import init_screen

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((COMPRIMENTO, LARGURA))
pygame.display.set_caption('1,2,3 BERTO')

state = TA_COMEÇANDO
while state != ACABOU:
    if state == TA_COMEÇANDO:
        state = init_screen(window)
    elif state == TA_ROLANDO:
        state = ACABOU
    else:
        state = ACABOU

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

