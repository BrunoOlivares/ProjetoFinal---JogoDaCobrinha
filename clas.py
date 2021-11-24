import pygame
speed=3

class cabeca(pygame.sprite.Sprite):
    
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

class corpo(pygame.sprite.Sprite):
    
    def __init__(self, imagem,x,y):

        pygame.sprite.Sprite.__init__(self)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_lefty=0
        self.change_righty=0
        self.change_upx=0
        self.change_downx=0
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
        self.change_lefty=0
        self.change_righty=0
        self.change_upx=0
        self.change_downx=0
        self.rect.x += self.speedx
        self.rect.y += self.speedy