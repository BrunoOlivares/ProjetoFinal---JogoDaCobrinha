from os import device_encoding
import pygame
from pygame import rect
from pygame.sprite import Sprite
from clas import cabeca,corpo


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

game = True

clock = pygame.time.Clock()
FPS = 50
cobra_completa=pygame.sprite.Group()
corpo_cobra = pygame.sprite.Group()
x = -15
y = 400
#cabeça e jogador

player=cabeca(img_jog,x,y)
cobra_completa.add(player)

#formação do corpo da cobra
x1=-30
posicao_corpo=[]
for i in range(8):
    pedaço_cobra = corpo(menor_cobra, x1, y)
    corpo_cobra.add(pedaço_cobra)
    x1 -= 15
cobra_completa.add(corpo_cobra)
pedaço_cobra.c
while game:

    clock.tick(FPS)

    for event in pygame.event.get():
        contador=0
        for parte in corpo_cobra:
            
            contador+=1

        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT and player.speedx == 0:
                if player.speedy<0:
                    dif=-15
                    player.rect.x=player.rect.x-15
                    player.speedx=-speed
                    player.speedy=0
                    pedaço_cobra
                if player.speedy>0:
                    dif=15
                    player.rect.x=player.rect.x-15
                    player.speedx=-speed
                    player.speedy=0
                    decisive_1=player.rect.y
                for parte in corpo_cobra:
                                        
                    if parte.rect.y == decisive_1 and parte.speedx != player.speedx:
                         parte.speedx=-speed
                         parte.speedy=0

            if event.key == pygame.K_RIGHT and player.speedx == 0:
                if player.speedy>0:
                    dif=15
                    player.rect.x=player.rect.x+15
                    player.speedx=speed
                    player.speedy=0
                    decisive_2=player.rect.y
                if player.speedy<0:
                    dif=-15
                    player.rect.x=player.rect.x+15
                    player.speedx=speed
                    player.speedy=0
                    decisive_2=player.rect.y
                for parte in corpo:
                    parte.rect.y+=dif
                    if parte.rect.y == decisive_2 and parte.speedx != player.speedx:
                        parte.speedx=speed
                        parte.speedy=0


            if event.key == pygame.K_UP and player.speedy == 0:
                if player.speedx<0:
                    dif=-15
                    player.rect.y=player.rect.y-15
                    player.speedx=0
                    player.speedy=-speed
                    decisive_3=player.rect.x
                if player.speedx>0:
                    dif=15
                    player.rect.y=player.rect.y-15
                    player.speedx=-0
                    player.speedy=-speed
                    decisive_3=player.rect.x
                for parte in corpo:
                    parte.rect.x+=dif
                    if parte.rect.x == decisive_3 and parte.speedy != player.speedy:
                        parte.speedx=0
                        parte.speedy=-speed

            if event.key == pygame.K_DOWN and player.speedy == 0:
                if player.speedx<0:
                    dif=-15
                    player.rect.y=player.rect.y+15
                    player.speedx=0
                    player.speedy=+speed
                    decisive_4=player.rect.x
                if player.speedx>0:
                    dif=15
                    player.rect.y=player.rect.y+15
                    player.speedx=-0
                    player.speedy=+speed
                    decisive_4=player.rect.x
                for parte in corpo:
                    parte.rect.x+=dif
                    if parte.rect.x == decisive_4 and parte.speedy != player.speedy:
                        parte.speedx=0
                        parte.speedy=speed
                        

       


    cobra_completa.update()

    janela_de_jogo.fill((0, 0, 0))
    cobra_completa.draw(janela_de_jogo)
    pygame.display.update()
pygame.quit()
print("hi")