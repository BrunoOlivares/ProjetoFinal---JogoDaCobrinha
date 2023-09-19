import pygame
import random
from Predefinicoes import settings

# criação da classe cabeça--------------------------------------

class cabeca(pygame.sprite.Sprite):

    def position(self,position):
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
         
    
    def __init__(self,animation,position):

        pygame.sprite.Sprite.__init__(self)
        self.lista=animation
        self.animacao=0
        self.dir_esq=0
        self.image = self.lista[self.dir_esq][self.animacao]
        self.position(position)
        self.speedx = settings.speed
        self.speedy = 0

    #função de update da cabeça com animação--------------------
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


#criação da classe Pedaço_Cobra -----------------------------
class Pedaco_Cobra(cabeca):

    def __init__(self, animation,list):
        super().__init__(animation,list)
        dir_esq=list[2]
        animacao=list[3]
        self.image = self.lista[dir_esq][animacao]
        super().position(list)

    def update(self):
        pass

#criação da classe fruta -----------------------------------

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