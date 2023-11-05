import pygame as pg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

WIDTH, HEIGHT = 500, 700

clock = pg.time.Clock()

class User:
    def __init__(self, x, y, width, height, dy, dx, gravity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = dy
        self.dx = dx
        self.gravity = gravity
        self.sprite1 = pg.image.load("Sprites/pixil-frame-0 (6).png")
        self.sprite2 = pg.image.load("Sprites/pixil-frame-0 (7).png")
        self.current_sprite = self.sprite2
        self.powered = False

    def draw(self, screen, left, right):
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)

        if self.powered == True:
            self.current_sprite = self.sprite1
        else: 
            self.current_sprite = self.sprite2
        
        screen.blit(self.current_sprite, self.hit_box)
        keys = pg.key.get_pressed()

        ### y direction
        self.dy += self.gravity
            
        if self.dy < 0:
            if self.y > 400:
                self.y += self.dy

        elif self.dy > 0:
            self.y += self.dy
        ###

        ### x direction
        if keys[left]:
            if self.dx > -10:
                self.dx -= 0.5
            self.x += self.dx
        
        if keys[right]:
            if self.dx < 10:
                self.dx += 0.5
            self.x += self.dx
        
        if not keys[left] and not keys[right]:
            if self.dx < 0:
                self.dx += 0.5
            if self.dx > 0:
                self.dx -= 0.5
            self.x += self.dx

        if self.x < -60:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = -60
        ###