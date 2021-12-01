#imports de bibliotecas e outros arquivos utilizados para criar o jogo
import pygame
import random
from Game_over import game_over_sreen
from Predefinicoes import GAME_OVER, LARGURA, COMPRIMENTO, TA_COMEÇANDO, TA_ROLANDO, ACABOU
from Tela_Inicial import init_screen
from Tela_principal import o_jogo

#iniciando o midulo do pygame e o mixer para colocar sons
pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
tela = pygame.display.set_mode((COMPRIMENTO, LARGURA))
pygame.display.set_caption('1,2,3 BERTO')

state = TA_COMEÇANDO
while state != ACABOU:      # para todo estado de jogo diferente de acabou o jogo esta rodando por meio do while

    if state == TA_COMEÇANDO:
        state = init_screen(tela) # para o estado de jogo "ta comecando" se inicia a tela inicial

    elif state == TA_ROLANDO:
        state = o_jogo(tela)    # para o estado de jogo "ta rolando" se inicia a tela principal do jogo

    elif state == GAME_OVER:
        state = game_over_sreen(tela)   # para o estado de jogo "game over" se inicia a tela final

    else:
        state = ACABOU      # finaliza o jogo

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados