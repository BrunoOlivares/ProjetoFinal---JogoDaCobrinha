from os import device_encoding
import pygame
from pygame.sprite import Sprite
from Predefinições import FPS, LARGURA, COMPRIMENTO, GAME_OVER, TA_ROLANDO, ACABOU
import random

def o_jogo(tela):

    background = pygame.image.load("Tela_principal.png").convert()
    background = pygame.transform.scale(background, (COMPRIMENTO, LARGURA))
    background_rect = background.get_rect()
    img_fruta = pygame.image.load("secao_cobra.png").convert_alpha()
    img_fruta = pygame.transform.scale(img_fruta, (25, 25))
    imagem_secao_cobraberto2 = pygame.image.load("2berto.png").convert_alpha()
    humberto_andando = pygame.transform.scale(imagem_secao_cobraberto2, (8, 8))
    speed = 25
    animacao_Humberto_direita = []
    animacao_Humberto_esquerda=[]
    animacao_tds=[]
    fonte_texto = pygame.font.SysFont(None, 20)

    for i in range(1, 5):

        animacao_esquerda = "Humberto2.0/Humberto_Esquerda_{}.png".format(i)
        animacao_esquerda = pygame.image.load(animacao_esquerda).convert_alpha()
        animacao_esquerda = pygame.transform.scale(animacao_esquerda, (25, 25))
        animacao_Humberto_esquerda.append(animacao_esquerda)
        animacao_direita = "Humberto2.0/Humberto_Direita_{}.png".format(i)
        animacao_direita = pygame.image.load(animacao_direita).convert_alpha()
        animacao_direita = pygame.transform.scale(animacao_direita, (25, 25))
        animacao_Humberto_direita.append(animacao_direita)

    animacao_tds.append(animacao_Humberto_direita)
    animacao_tds.append(animacao_Humberto_esquerda)
    coordenadas_xy_pedaços = []
    pedaços_da_cobra = pygame.sprite.Group()
    rabo_da_cobra = pygame.sprite.Group()
    frutinhaG=pygame.sprite.Group()

    class Cabeça(pygame.sprite.Sprite):

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

            if self.animacao > 3:
                self.animacao=0

            if self.speedy != 0:
                self.animacao += 1
            
            if self.animacao > 3:
                self.animacao = 0

            self.image=self.lista[self.dir_esq][self.animacao]
            self.rect.x += self.speedx
            self.rect.y += self.speedy

    class Pedaço_Cobra(pygame.sprite.Sprite):

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
    bertos=1
    x = 300
    y = 300

    #cabeça e jogador
    changey=-200
    player = Cabeça(animacao_tds,x,y)
    pedaços_da_cobra.add(player)
    frutola=fruta(img_fruta,COMPRIMENTO,LARGURA)
    frutinhaG.add(frutola)
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
            apertou=False

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
            
            pedaco = Pedaço_Cobra(animacao_tds, cordenada_x, cordenada_y, dir_esq, animacao)

            if apertou==True:
                if player.speedx < 0:
                    pedaco.dir_esq=1
                if player.speedy !=0 and changey==pedaco.rect.y:
                    pedaco.image==player.image
                if player.speedx > 0:
                    pedaco.dir_esq=0

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

        col = pygame.sprite.spritecollide(player, frutinhaG, False)

        if len(col) > 0:
            bertos+=1
            frutinhaG.empty()

        tela.blit(background, background_rect)
        pedaços_da_cobra.draw(tela)
        frutinhaG.draw(tela)

        pontuacao = fonte_texto.render("Numero de Bertos: {}". format(bertos), True, (120, 255, 120))
        tela.blit(pontuacao, (17, 325))

        pygame.display.update()

        if len(frutinhaG)==0:
            frutola=fruta(img_fruta,COMPRIMENTO,LARGURA)
            frutinhaG.add(frutola)
    return estado_de_jogo

    

