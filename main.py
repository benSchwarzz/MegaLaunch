import pygame as pg
import random, math
pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 500
HEIGHT = 700
screen = pg.display.set_mode((WIDTH, HEIGHT))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0
        self.dx = 0
        self.sprite = pg.image.load("SpaceShip Adventure/images/pixil-frame-0 (6).png")
        self.sprite2 = pg.image.load("SpaceShip Adventure/images/pixil-frame-0 (7).png")
        self.current_sprite = self.sprite2
    
    def update(self):
        hit_box = pg.Rect(self.x, self.y, 60, 100)
        screen.blit(self.current_sprite, hit_box)

    def move(self, left, right, hitbox):
        keys = pg.key.get_pressed()


        if keys[right]:
            if self.x > WIDTH - 30:
                if self.dx < 8:
                    self.dx += 0.5

        if keys[left]:
            if self.x < 0:
                if self.dx > -8:
                    self.dx -=0.5

        if not keys[left] and not keys[right]:
            self.dx = 0
        
        self.x += self.dx


def main():
    player = Player(235, (HEIGHT - 100))

    run = True
    while run:
        screen.fill(WHITE)

        player.update()
        player.move(pg.K_w, pg.K_a, pg.K_d)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
    pg.quit()

main()
