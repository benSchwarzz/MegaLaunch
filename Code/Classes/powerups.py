import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

WIDTH, HEIGHT = 500, 700

clock = pg.time.Clock()

class Powerup:
    def __init__(self, x, height, width, dy):
        self.x = x
        self.y = -70
        self.width = width
        self.height = height
        self.dy = dy
        self.type = None

class Speed_boost(Powerup):
    def draw(self, screen):
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)
        self.sprite = pg.image.load("Sprites/speed_boost.png")
        screen.blit(self.sprite, self.hit_box)
        self.y += self.dy
        self.type = "speed_boost"

class Oil_boost(Powerup):
    def draw(self, screen):
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)
        self.sprite = pg.image.load("Sprites/pixil-frame-0 (11).png")
        screen.blit(self.sprite, self.hit_box)
        self.y += self.dy
        self.type = "oil_boost"