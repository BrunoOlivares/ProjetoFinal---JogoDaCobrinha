def cria_fruta():
    from os import device_encoding
    import pygame
    from pygame.sprite import Sprite
    import random
    contador_fruta = 0
    tempo_atual = 0
    while contador_fruta < 10:
        tempo_atual = pygame.time.get_ticks()
        
        if tempo_atual > 5000:
            fruta = comida(img_jog)
            pedaços_da_cobra.add(fruta)
            contador_fruta += 1
            tempo_atual = 0

