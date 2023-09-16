import pygame
import random
from Predefinicoes import settings

# criação da classe cabeça--------------------------------------

class cabeca(pygame.sprite.Sprite):

    def position(self,x,y):
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def img(self,d_e,animation):
        self.image = self.lista[self.dir_esq][self.animacao]

        
    
    def __init__(self,lista,x,y):

        pygame.sprite.Sprite.__init__(self)
        self.lista=lista
        self.animacao=0
        self.dir_esq=0
        self.image = self.lista[self.dir_esq][self.animacao]
        self.position(x,y)
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

    def __init__(self, lista_, x_, y_, dir_esq, animacao):
        super().__init__(lista_,x_,y_)
        self.image = self.lista[dir_esq][animacao]
        super().position(x_,y_)

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