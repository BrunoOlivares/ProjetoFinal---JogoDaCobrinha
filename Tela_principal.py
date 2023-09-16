#imports de bibliotecas e outros arquivos utilizados para criar o jogo

from os import device_encoding
import pygame
from pygame.sprite import Sprite
from Predefinicoes import settings
from assets import load_assets
import random
from clas import cabeca , fruta , Pedaco_Cobra

#função para iniciar o jogo-------------------------------------
def o_jogo(tela):
    #importar da pasta assets as imagens e musicas-------------------
    assets=load_assets()
    bg=assets['bg principal']
    bg_rect=assets['bg rect principal']
    imagem_fruta=assets['imagem da fruta']
    fonte=assets['fonte do texto']
    musica_durante=assets['musica durante jogo']
    animacoes_berto=assets['animações']
    bertos=1
    pedaços_da_cobra = pygame.sprite.Group()
    rabo_da_cobra = pygame.sprite.Group()
    frutinhaG=pygame.sprite.Group()
    pygame.mixer.music.load(musica_durante)
    pygame.mixer.music.set_volume(0.2)
    #----------------------------------------------------------

    estado_de_jogo = settings.happening

    clock = pygame.time.Clock()

    #cabeça e jogador --------------------------------------------------------------
    player = cabeca(animacoes_berto,settings.x_inicial,settings.y_inicial)
    pedaços_da_cobra.add(player)
    frutola=fruta(imagem_fruta,settings.length,settings.width)
    frutinhaG.add(frutola)
    
    #loop da musica durante a partida-----------------------------------------------
    pygame.mixer.music.play(loops=-1)
    
    #spawn da fruta apos colisão-------------------------------------------------------
    while estado_de_jogo == settings.happening:
        for pedaco in pedaços_da_cobra:
            continuar=False
            while continuar:
                if frutola.rect.x == pedaco.rect.x and frutola.rect.y== pedaco.rect.y:     
                    frutola.rect.x=random.randint(0,settings.length)
                    frutola.rect.y=random.randint(0,settings.width) 
                continuar=True
        
        clock.tick(settings.fps)
        for event in pygame.event.get():

            if event.type == pygame.QUIT: 

                estado_de_jogo = settings.over    # fim do jogo
             

            if event.type == pygame.KEYDOWN:

                apertou=True

                # Dependendo da tecla, altera a velocidade para trocar de direção
                if event.key == pygame.K_LEFT and player.speedx == 0:

                    player.speedx = -settings.speed
                    player.speedy = 0

                if event.key == pygame.K_RIGHT and player.speedx == 0:

                    player.speedx = settings.speed
                    player.speedy = 0

                if event.key == pygame.K_UP and player.speedy == 0:

                    player.speedx = 0
                    player.speedy = -settings.speed

                if event.key == pygame.K_DOWN and player.speedy == 0:

                    player.speedx = 0
                    player.speedy = settings.speed

                if event.key == pygame.K_0:

                    estado_de_jogo = settings.game_over
        
        player.update()
        
        #verifica o tamanho da cobra com o tamanho da lista
        if len(settings.coordenadas_xy_pedaços) > bertos:
            del settings.coordenadas_xy_pedaços[0]

        for rabo in rabo_da_cobra.sprites():

            rabo.kill()

        rabo_da_cobra.empty()
        
        #verifica colisão com a fruta e tambem aumenta o tamanho da cobra
        col = pygame.sprite.spritecollide(player, frutinhaG, False)

        if len(col) > 0:
            bertos+=1
            frutinhaG.empty()

        settings.coordenadas_xy_pedaços.append([player.rect.x, player.rect.y, player.dir_esq, player.animacao])

        for i in range(1,bertos):

            coordenada = settings.coordenadas_xy_pedaços[len(settings.coordenadas_xy_pedaços)-i-1]
            cordenada_x = coordenada[0]
            cordenada_y = coordenada[1]

            dir_esq = coordenada[2]
            animacao = coordenada[3]
            
            pedaco = Pedaco_Cobra(animacoes_berto, cordenada_x, cordenada_y, dir_esq, animacao)
            rabo_da_cobra.add(pedaco)
            #print(coordenadas_xy_pedaços)

        rabo_da_cobra.update()
        pedaços_da_cobra.add(rabo_da_cobra)
        
        # teste de colisão
        hit = pygame.sprite.spritecollide(player, rabo_da_cobra, False)

        #delimitações da area de jogo ----------------------------------------------
        if len(hit) > 0:
    
            estado_de_jogo = settings.game_over

        if player.rect.x == 200:
            estado_de_jogo = settings.game_over

        if player.rect.x == 1200:
            estado_de_jogo = settings.game_over

        if player.rect.y == 50:
            estado_de_jogo = settings.game_over

        if player.rect.y == 900:
            estado_de_jogo = settings.game_over
        
        if estado_de_jogo == settings.game_over:
            pygame.mixer.music.stop()
        #colisão com a fruta = aumento de tamanho---------------------------------------------------------
        col = pygame.sprite.spritecollide(player, frutinhaG, False)

        if len(col) > 0:
            bertos+=1
            frutinhaG.empty()
        
        tela.blit(bg, bg_rect)
        pedaços_da_cobra.draw(tela)
        frutinhaG.draw(tela)

        #print da pontuação ------------------------------------------------------------------------------

        pontuacao = fonte.render("Numero de Bertos: {}". format(bertos), True, (120, 255, 120))
        tela.blit(pontuacao, (17, 325))

        pygame.display.update()

        if len(frutinhaG)==0:
            frutola=fruta(imagem_fruta,settings.length,settings.width)
            frutinhaG.add(frutola)

    return estado_de_jogo
    

