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
    tamanho_cobra = 10

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

            if self.rect.left > 1120 and self.speedx > 0 :
                self.rect.x = -120
            if self.rect.left < 5 and self.speedx < 0 :
                self.rect.x = 1115
            if self.rect.top < 5 and self.speedy < 0:
                self.rect.y = 795
            if self.rect.top > 800 and self.speedy > 0:
                self.rect.top = 6

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
    FPS = 15

    x = 300
    y = 400

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

        player.update()

        coordenadas_xy_pedaços.append([player.rect.x, player.rect.y])

        if len(coordenadas_xy_pedaços) > tamanho_cobra:
            del coordenadas_xy_pedaços[0]

        for rabo in rabo_da_cobra.sprites():

            rabo.kill()

        rabo_da_cobra.empty()

        for coordenada in coordenadas_xy_pedaços:

            pedaço = Pedaço_Cobra(humberto_parado, coordenada[0], coordenada[1])
            rabo_da_cobra.add(pedaço)
            print(coordenadas_xy_pedaços)

        rabo_da_cobra.update()
        tela.blit(background, background_rect)
        pedaços_da_cobra.draw(tela)
        rabo_da_cobra.draw(tela)

        pygame.display.update()

    return estado_de_jogo

    

