#import de bibliotecas ou arquivos do jogo
from Predefinicoes import GAME_OVER, LARGURA, COMPRIMENTO
import pygame




def load_assets():    # função para dar load e ajustar as imagens e sons utilizados durante o jogo
    assets={}
    background_principal = pygame.image.load("telas do jogo\Tela_principal.png").convert()       #tela principal
    background_principal = pygame.transform.scale(background_principal, (COMPRIMENTO, LARGURA))
    background_principal_rect = background_principal.get_rect()
    background_game_over = pygame.image.load('telas do jogo\Tela_de_game_over.png').convert()   #tela para game over
    background_game_over = pygame.transform.scale(background_game_over, (COMPRIMENTO, LARGURA))
    background_game_over_rect = background_game_over.get_rect()
    background_inicial = pygame.image.load('telas do jogo\Tela_inicial_ctexto.png').convert()    #tela de inicio
    background_inicial = pygame.transform.scale(background_inicial, (COMPRIMENTO, LARGURA))
    background_inicial_rect = background_inicial.get_rect()

    assets['bg principal']=background_principal
    assets['bg rect principal']=background_principal_rect
    assets['bg inicial']=background_inicial
    assets['bg rect inicial']=background_inicial_rect
    assets['bg game over']=background_game_over
    assets['bg rect game over']=background_game_over_rect


    # imagem fruta--------------------------------------------------------------------
    img_fruta = pygame.image.load("animações\Fruta_py.png").convert_alpha()  
    img_fruta = pygame.transform.scale(img_fruta, (25, 25))

    assets['imagem da fruta']=img_fruta

    animacao_Humberto_direita = []
    animacao_Humberto_esquerda=[]
    animacao_tds=[]
    fonte_texto = pygame.font.SysFont(None, 20)

    #catalogando as musicas para serem utiliizadas----------------------------------

    assets['fonte do texto']=fonte_texto
    assets['musica menu']='musicas\musica_menu.mp3'
    assets['musica durante jogo']='musicas\musica_tela_principal.mp3'
    assets['musica game over']='musicas\game_over.wav'
        

    #animação do personagem do jogo-------------------------------------------------
    for i in range(1, 5):

        animacao_esquerda = "animações\Humberto\Humberto_Esquerda_{}.png".format(i)
        animacao_esquerda = pygame.image.load(animacao_esquerda).convert_alpha()
        animacao_esquerda = pygame.transform.scale(animacao_esquerda, (25, 25))
        animacao_Humberto_esquerda.append(animacao_esquerda)
        animacao_direita = "animações\Humberto\Humberto_Direita_{}.png".format(i)
        animacao_direita = pygame.image.load(animacao_direita).convert_alpha()
        animacao_direita = pygame.transform.scale(animacao_direita, (25, 25))
        animacao_Humberto_direita.append(animacao_direita)

    animacao_tds.append(animacao_Humberto_direita)         #lista para a animação
    animacao_tds.append(animacao_Humberto_esquerda)
    assets['animações']=animacao_tds
    return assets

    #-------------------------------------------------------------------------------