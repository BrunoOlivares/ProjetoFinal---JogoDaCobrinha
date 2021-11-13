import pygame

pygame.init()

janela_de_jogo = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("1,2,3 Berto")

























game = True

while game:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game = False



    janela_de_jogo.fill((0, 0, 0))

    pygame.display.update()


pygame.quit()