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

settings.situation_game(init_screen,o_jogo,game_over_sreen,tela)
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados