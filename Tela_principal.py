from os import device_encoding
import pygame
from pygame.sprite import Sprite
from Predefinições import LARGURA, COMPRIMENTO, GAME_OVER, TA_ROLANDO, ACABOU

def o_jogo(tela):

    background = pygame.image.load("Tela_principal.png").convert()
    background = pygame.transform.scale(background, (COMPRIMENTO, LARGURA))
    background_rect = background.get_rect()
    imagem_secao_cobraberto1 = pygame.image.load("1,2,3_Berto_Anim/1berto.png").convert_alpha()
    humberto_parado = pygame.transform.scale(imagem_secao_cobraberto1, (25, 25))
    imagem_secao_cobraberto2 = pygame.image.load("2berto.png").convert_alpha()
    humberto_andando = pygame.transform.scale(imagem_secao_cobraberto2, (25, 25))
    speed = 30
    animacao_Humberto = []
    tamanho_cobra = 25

    for i in range(1, 6):

        animacao = "1,2,3_Berto_Anim/{}berto.png".format(i)
        animacao = pygame.image.load(animacao).convert_alpha()
        animacao = pygame.transform.scale(animacao, (30, 30))
        animacao_Humberto.append(animacao)

    coordenadas_xy_pedaços = []
    pedaços_da_cobra = pygame.sprite.Group()
    rabo_da_cobra = pygame.sprite.Group()

    class Cabeça(pygame.sprite.Sprite):

        def __init__(self, imagem,x,y):

            pygame.sprite.Sprite.__init__(self)

            self.image = imagem
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speedx = speed
            self.speedy = 0

        def update(self):

            self.rect.x += self.speedx
            self.rect.y += self.speedy

    class Pedaço_Cobra(pygame.sprite.Sprite):

        def __init__(self, imagem, x, y):

            pygame.sprite.Sprite.__init__(self)

            self.image = imagem
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speedx = speed
            self.speedy = 0

        def update(self):
            pass

    estado_de_jogo = TA_ROLANDO

    clock = pygame.time.Clock()
    FPS = 10

    x = 300
    y = 300

    #cabeça e jogador

    player = Cabeça(humberto_parado,x,y)
    pedaços_da_cobra.add(player)

    while estado_de_jogo == TA_ROLANDO:

        clock.tick(FPS)

        print(coordenadas_xy_pedaços)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                estado_de_jogo = ACABOU

            if event.type == pygame.KEYDOWN:

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

        coordenadas_xy_pedaços.append([player.rect.x, player.rect.y])        
        player.update()

        if len(coordenadas_xy_pedaços) > tamanho_cobra:
            del coordenadas_xy_pedaços[0]

        for rabo in rabo_da_cobra.sprites():

            rabo.kill()

        rabo_da_cobra.empty()

        for i in range(1, len(coordenadas_xy_pedaços)):

            coordenada = coordenadas_xy_pedaços[i]

            pedaço = Pedaço_Cobra(humberto_parado, coordenada[0], coordenada[1])
            rabo_da_cobra.add(pedaço)
            #print(coordenadas_xy_pedaços)

        rabo_da_cobra.update()

        hit = pygame.sprite.spritecollide(player, rabo_da_cobra, False)

        if len(hit) > 0:

            estado_de_jogo = GAME_OVER

        if player.rect.x == 0:
            estado_de_jogo = GAME_OVER

        if player.rect.x == 1200:
            estado_de_jogo = GAME_OVER

        if player.rect.y == 0:
            estado_de_jogo = GAME_OVER

        if player.rect.y == 900:
            estado_de_jogo = GAME_OVER

        tela.blit(background, background_rect)
        pedaços_da_cobra.draw(tela)
        rabo_da_cobra.draw(tela)

        pygame.display.update()

    return estado_de_jogo

    

