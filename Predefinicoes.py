class config():
    def __init__(self) -> None:   
        self.width = 900
        self.length = 1200

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
        

settings = config()
