#imports de bibliotecas e outros arquivos utilizados para criar o jogo
import pygame
import random
from Game_over import game_over_sreen
from Predefinicoes import settings
from Tela_Inicial import init_screen
from Tela_principal import o_jogo

#iniciando o módulo do pygame e o mixer para colocar sons
pygame.init()
pygame.mixer.init()

#Geração de tela atual em relação ao estado do jogo-----------------

tela = pygame.display.set_mode((settings.length, settings.width))
pygame.display.set_caption('1,2,3 BERTO')

state = settings.start
while state != settings.over:      # para todo estado de jogo diferente de acabou o jogo esta rodando por meio do while

    if state == settings.start:
        state = init_screen(tela) # para o estado de jogo "ta comecando" se inicia a tela inicial

    elif state == settings.happening:
        state = o_jogo(tela)    # para o estado de jogo "ta rolando" se inicia a tela principal do jogo

    elif state == settings.game_over:
        state = game_over_sreen(tela)   # para o estado de jogo "game over" se inicia a tela final

    else:
        state = settings.over      # finaliza o jogo

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados