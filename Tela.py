import pygame

pygame.init()

janela_de_jogo = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("1,2,3 Berto")

largura_cobra = 30
comprimento_cobra = 30
imagem_secao_cobra = pygame.image.load("secao_cobra.png").convert()
menor_cobra = pygame.transform.scale(imagem_secao_cobra, (15, 15))


class Cobra(pygame.sprite.Sprite):

    def __init__(self, imagem, posição_x, posição_y):

        pygame.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = posição_x
        self.rect.y = posição_y
        self.speedx = 3
        self.speedy = 0

    def update(self):

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left > 1120:
            self.rect.x = -120
            self.rect.y = 400
            self.speedx = 3
            self.speedy = 0

game = True

clock = pygame.time.Clock()
FPS = 200

pedaços_da_cobra = pygame.sprite.Group()

x = -15
y = 400

for i in range(4):

    pedaço_cobra = Cobra(menor_cobra, x, y)
    pedaços_da_cobra.add(pedaço_cobra)
    x -= 15

while game:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game = False

    pedaços_da_cobra.update()

    janela_de_jogo.fill((0, 0, 0))
    pedaços_da_cobra.draw(janela_de_jogo)

    pygame.display.update()

pygame.quit()