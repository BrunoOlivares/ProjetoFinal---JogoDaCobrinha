import pygame
class config():

    def __init__(self) -> None:   
        self.width = 900
        self.length = 1200
        self.position_phrase=(120, 255, 120)
        self.position_score=(17, 325)

        #Estados de jogo-----------------------------------

        self.over = 0
        self.game_over = 1
        self.start = 2
        self.happening = 3

        #FPS-----------------------------------------------

        self.fps = 20

        #lista das cordenadas da cobra---------------------

        self.coordenadas_xy_pedaços = []

        # variaveis----------------------------------------

        self.speed = 25

        self.bertinhos=1

        self.x_inicial = 300

        self.y_inicial = self.x_inicial

        #--------------------------------------------------

    def game_limitations(self,position,list,e):
        if len(list) > 0:
            e = self.game_over

        if position[0] == 200:
            e = self.game_over

        if position[0] == 1200:
            e = self.game_over

        if position[1] == 50:
            e = self.game_over

        if position[1] == 900:
            e = self.game_over
        
        if e == self.game_over:
            pygame.mixer.music.stop()
        return e
        
    def situation_game(self,init,o_jogo,gameover,tela):
        state = self.start
        while state != self.over:      # para todo estado de jogo diferente de acabou o jogo esta rodando por meio do while

            if state == self.start:
                state = init(tela) # para o estado de jogo "ta comecando" se inicia a tela inicial

            elif state == self.happening:
                state = o_jogo(tela)    # para o estado de jogo "ta rolando" se inicia a tela principal do jogo

            elif state == self.game_over:
                state = gameover(tela)   # para o estado de jogo "game over" se inicia a tela final

            else:
                state = self.over      # finaliza o jogo
    
        

settings = config()
