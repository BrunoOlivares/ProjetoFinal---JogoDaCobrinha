import pygame
import random
from Predefinições import speed

class cabeca(pygame.sprite.Sprite):

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