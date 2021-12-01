from os import device_encoding
import pygame
from pygame.sprite import Sprite
from Predefinicoes import FPS, LARGURA, COMPRIMENTO, GAME_OVER, TA_ROLANDO, ACABOU,coordenadas_xy_pedaços,speed,x_inicial,y_inicial
from assets import load_assets
import random

def o_jogo(tela):
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

    class Cabeca(pygame.sprite.Sprite):

        def __init__(self,lista,x,y):

            pygame.sprite.Sprite.__init__(self)
            self.lista=lista
            self.animacao=0
            self.dir_esq=0
            self.image = self.lista[self.dir_esq][self.animacao]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speedx = speed
            self.speedy = 0

        def update(self):

            if self.speedx > 0:
                self.dir_esq=0
                self.animacao+=1


            if self.speedx < 0:
                self.dir_esq=1
                self.animacao+=1
            
            if self.speedy > 0 or self.speedy<0:
                self.animacao+=1


            if self.animacao > 3:
                self.animacao=0

            if self.speedy != 0:
                self.animacao += 1
            
            if self.animacao > 3:
                self.animacao = 0

            self.image=self.lista[self.dir_esq][self.animacao]
            self.rect.x += self.speedx
            self.rect.y += self.speedy

    class Pedaco_Cobra(pygame.sprite.Sprite):

        def __init__(self, lista, x, y, dir_esq, animacao):

            pygame.sprite.Sprite.__init__(self)
            
            self.all=lista
            self.image = self.all[dir_esq][animacao]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


        def update(self):

            pass

    
    class fruta (pygame.sprite.Sprite):
        def __init__(self,img,comprimento,largura):
            pygame.sprite.Sprite.__init__(self)
            x=random.randint(200, comprimento-90)
            y=random.randint(50, largura-60)
            self.image=img
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y
        def update(self):
            pass

    estado_de_jogo = TA_ROLANDO

    clock = pygame.time.Clock()

    #cabeça e jogador
    player = Cabeca(animacoes_berto,x_inicial,y_inicial)
    pedaços_da_cobra.add(player)
    frutola=fruta(imagem_fruta,COMPRIMENTO,LARGURA)
    frutinhaG.add(frutola)
    pygame.mixer.music.play(loops=-1)
    while estado_de_jogo == TA_ROLANDO:
        for pedaco in pedaços_da_cobra:
            continuar=False
            while continuar:
                if frutola.rect.x == pedaco.rect.x and frutola.rect.y== pedaco.rect.y:
                    frutola.rect.x=random.randint(0,COMPRIMENTO)
                    frutola.rect.y=random.randint(0,LARGURA)
                continuar=True
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                estado_de_jogo = ACABOU
             

            if event.type == pygame.KEYDOWN:

                apertou=True

                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT and player.speedx == 0:

                    player.speedx = -speed
                    player.speedy = 0

                if event.key == pygame.K_RIGHT and player.speedx == 0:

                    player.speedx = speed
                    player.speedy = 0

                if event.key == pygame.K_UP and player.speedy == 0:

                    player.speedx = 0
                    player.speedy = -speed

                if event.key == pygame.K_DOWN and player.speedy == 0:

                    player.speedx = 0
                    player.speedy = speed

                if event.key == pygame.K_0:

                    estado_de_jogo = GAME_OVER
        
        player.update()
        

        if len(coordenadas_xy_pedaços) > bertos:
            del coordenadas_xy_pedaços[0]

        for rabo in rabo_da_cobra.sprites():

            rabo.kill()

        rabo_da_cobra.empty()

        col = pygame.sprite.spritecollide(player, frutinhaG, False)

        if len(col) > 0:
            bertos+=1
            frutinhaG.empty()

        coordenadas_xy_pedaços.append([player.rect.x, player.rect.y, player.dir_esq, player.animacao])

        for i in range(1,bertos):

            coordenada = coordenadas_xy_pedaços[len(coordenadas_xy_pedaços)-i-1]
            cordenada_x = coordenada[0]
            cordenada_y = coordenada[1]

            dir_esq = coordenada[2]
            animacao = coordenada[3]
            
            pedaco = Pedaco_Cobra(animacoes_berto, cordenada_x, cordenada_y, dir_esq, animacao)
            rabo_da_cobra.add(pedaco)
            #print(coordenadas_xy_pedaços)

        rabo_da_cobra.update()
        pedaços_da_cobra.add(rabo_da_cobra)

        hit = pygame.sprite.spritecollide(player, rabo_da_cobra, False)

        if len(hit) > 0:

            estado_de_jogo = GAME_OVER

        if player.rect.x == 200:
            estado_de_jogo = GAME_OVER

        if player.rect.x == 1200:
            estado_de_jogo = GAME_OVER

        if player.rect.y == 50:
            estado_de_jogo = GAME_OVER

        if player.rect.y == 900:
            estado_de_jogo = GAME_OVER
        
        if estado_de_jogo == GAME_OVER:
            pygame.mixer.music.stop()

        col = pygame.sprite.spritecollide(player, frutinhaG, False)

        if len(col) > 0:
            bertos+=1
            frutinhaG.empty()

        tela.blit(bg, bg_rect)
        pedaços_da_cobra.draw(tela)
        frutinhaG.draw(tela)

        pontuacao = fonte.render("Numero de Bertos: {}". format(bertos), True, (120, 255, 120))
        tela.blit(pontuacao, (17, 325))

        pygame.display.update()

        if len(frutinhaG)==0:
            frutola=fruta(imagem_fruta,COMPRIMENTO,LARGURA)
            frutinhaG.add(frutola)

    return estado_de_jogo
    

