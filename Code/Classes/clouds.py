import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

WIDTH, HEIGHT = 500, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

class Cloud:
    def __init__(self, x, dy):
        self.x = x
        self.y = -50
        self.width = 100
        self.height = 50
        self.dy = dy
        self.sprite = pg.image.load("Sprites/pixil-frame-0 (8).png")
        
    
    def draw(self):
        self.box = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.sprite, self.box)

        self.y += self.dy