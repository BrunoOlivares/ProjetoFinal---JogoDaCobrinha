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
speed=3

class Cobra(pygame.sprite.Sprite):

    def __init__(self, imagem,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = speed
        self.speedy = 0

    def update(self):

        if self.rect.left > 1120 and self.speedx>0 :
            self.rect.x = -120
        if self.rect.left < 5 and self.speedx<0 :
            self.rect.x=1115
        if self.rect.top<5 and self.speedy<0:
            self.rect.y=795
        if self.rect.top >800 and self.speedy>0:
            self.rect.top=6



        self.rect.x += self.speedx
        self.rect.y += self.speedy

game = True

clock = pygame.time.Clock()
FPS = 200

pedaços_da_cobra = pygame.sprite.Group()
x = -15
y = 400
#cabeça e jogador
player=Cobra(img_jog,x,y)
pedaços_da_cobra.add(player)

#formação do corpo da cobra
x1=-30
posicao_corpo=[]
for i in range(8):
    pedaço_cobra = Cobra(menor_cobra, x1, y)
    pedaços_da_cobra.add(pedaço_cobra)
    x1 -= 15

while game:

    clock.tick(FPS)

    for event in pygame.event.get():
        contador=0
        for parte in pedaços_da_cobra:
            contador+=1

        if event.type == pygame.QUIT:

            game = False

        if event.type == pygame.KEYDOWN:
            control=True
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT and player.speedx == 0:
                player.speedx=-speed
                player.speedy=0
                decisive_1 = player.rect.y
                cont=0
                while control:
                    for parte in pedaços_da_cobra:
                        if parte.rect.y == decisive_1 and parte.speedx != player.speedx:
                            parte.speedx=-speed
                            parte.speedy=0
                            cont+=1
                        if cont == contador :
                            control=False
            if event.key == pygame.K_RIGHT and player.speedx == 0:
                player.speedx=speed
                player.speedy=0
                decisive_2=player.rect.y
                cont=0
                while control:
                    for parte in pedaços_da_cobra:
                        if parte.rect.y == decisive_2 and parte.speedx != player.speedx:
                            parte.speedx=speed
                            parte.speedy=0
                            cont+=1
                        if cont == contador :
                            control=False

            if event.key == pygame.K_UP and player.speedy == 0:
                player.speedx=-0
                player.speedy=-speed
                decisive_3=player.rect.x
                cont=0
                while control:
                    for parte in pedaços_da_cobra:
                        if parte.rect.y == decisive_3 and parte.speedy != player.speedy:
                            parte.speedx=0
                            parte.speedy=-speed
                            cont+=1
                        if cont == contador :
                            control=False

            if event.key == pygame.K_DOWN and player.speedy == 0:
                player.speedx=0
                player.speedy=speed
                decisive_4=player.rect.x
                cont=0
                while control:
                    for parte in pedaços_da_cobra:
                        if parte.rect.y == decisive_4 and parte.speedy != player.speedy:
                            parte.speedx=0
                            parte.speedy=speed
                            cont+=1
                        if cont == contador :
                            control=False

    pedaços_da_cobra.update()

    janela_de_jogo.fill((0, 0, 0))
    pedaços_da_cobra.draw(janela_de_jogo)
    pygame.display.update()
pygame.quit()

print("hi")