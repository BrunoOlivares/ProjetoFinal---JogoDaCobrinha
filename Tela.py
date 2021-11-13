import pygame

pygame.init()

janela_de_jogo = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("1,2,3 Berto")

largura_cobra = 30
comprimento_cobra = 30
imagem_secao_cobra = pygame.image.load("secao_cobra.png").convert()
menor_cobra = pygame.transform.scale(imagem_secao_cobra, (15, 15))

game = True

posicao_cobra_x = -120
posicao_cobra_y = 400
velocidade_da_cobra_x = 3
velocidade_da_cobra_y = 0

clock = pygame.time.Clock()
FPS = 200


while game:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game = False

    posicao_cobra_x += velocidade_da_cobra_x
    posicao_cobra_y += velocidade_da_cobra_y

    if posicao_cobra_x > 1000:
        posicao_cobra_x = -30
 
    janela_de_jogo.fill((0, 0, 0))
    janela_de_jogo.blit(menor_cobra, (posicao_cobra_x, posicao_cobra_y))
    janela_de_jogo.blit(menor_cobra, (posicao_cobra_x - 15, posicao_cobra_y))
    janela_de_jogo.blit(menor_cobra, (posicao_cobra_x - 30, posicao_cobra_y))
    janela_de_jogo.blit(menor_cobra, (posicao_cobra_x - 45, posicao_cobra_y))


    pygame.display.update()


pygame.quit()