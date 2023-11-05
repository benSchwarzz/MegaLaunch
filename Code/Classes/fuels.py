import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

WIDTH, HEIGHT = 500, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

class Fuel:
    def __init__(self, x, dy):
        self.width = 25
        self.height = 41
        self.x = x
        self.y = -42
        self.dy = dy
        self.image = pg.image.load("Sprites/pixil-frame-0 (9).png")
        self.sprite = pg.transform.scale(self.image, (25, 41))
    
    def draw(self):
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.sprite, self.hit_box)

        self.y += self.dy