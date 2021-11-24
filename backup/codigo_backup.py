from os import device_encoding
import pygame
from pygame.sprite import Sprite

pygame.init()

janela_de_jogo = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("1,2,3 Berto")

largura_cobra = 30
comprimento_cobra = 30
imagem_secao_cobra = pygame.image.load("secao_cobra.png").convert()
menor_cobra = pygame.transform.scale(imagem_secao_cobra, (15, 15))
imagem_jogador = pygame.image.load("player.png").convert()
img_jog= pygame.transform.scale(imagem_jogador, (15, 15))
speed = 15
tamanho_cobra = 0

coordenadas_xy_pedaços = []
pedaços_da_cobra = pygame.sprite.Group()

class Cabeça(pygame.sprite.Sprite):

    def __init__(self, imagem,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speed
        self.speedy = 0

        coordenadas_xy_pedaços.append([self.rect.x, self.rect.y])
        pedaços_da_cobra.add(self)

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


        coordenadas_xy_pedaços.append([self.rect.x, self.rect.y])
        del coordenadas_xy_pedaços[0]

class Pedaços_Cobra(pygame.sprite.Sprite):

    def __init__(self, imagem):

        pygame.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = coordenadas_xy_pedaços[0][0]
        self.rect.y = coordenadas_xy_pedaços[0][1]

        coordenadas_xy_pedaços.append([self.rect.x, self.rect.y])
        pedaços_da_cobra.add(self)

    def update(self):

        self.rect.x = coordenadas_xy_pedaços[0][0]
        self.rect.y = coordenadas_xy_pedaços[0][1]

        coordenadas_xy_pedaços.append([self.rect.x, self.rect.y])
        del coordenadas_xy_pedaços[0]

game = True

clock = pygame.time.Clock()
FPS = 30

x = 300
y = 400

#cabeça e jogador

player = Cabeça(img_jog,x,y)
fruta = Pedaços_Cobra(img_jog)

while game:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game = False

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

    print(coordenadas_xy_pedaços)

    pedaços_da_cobra.update()

    janela_de_jogo.fill((0, 0, 0))
    pedaços_da_cobra.draw(janela_de_jogo)
    pygame.display.update()

pygame.quit()
