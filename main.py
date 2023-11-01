import pygame as pg
import random, math
pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

WIDTH, HEIGHT = 500, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

class User:
    def __init__(self, x, y, width, height, dy, dx):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dy = dy
        self.dx = dx
        self.sprite1 = pg.image.load("SpaceShip Adventure/images/pixil-frame-0 (6).png")
        self.sprite2 = pg.image.load("SpaceShip Adventure/images/pixil-frame-0 (7).png")
        self.current_sprite = self.sprite2
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(self.current_sprite, self.hit_box)
    
class Cloud:
    def __init__(self, y, width, height, dy):
        self.x = random.randint(-40, WIDTH -20)
        self.y = y
        self.width = width
        self.height = height
        self.dy = dy
        self.sprite = pg.image.load("SpaceShip Adventure/images/pixil-frame-0 (8).png")
        
    
    def draw(self):
        self.box = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.sprite, self.box)
    def move(self):
        self.y += self.dy

        if self.y > HEIGHT+40:
            pg.time.wait(random.randint(50, 200))
            self.y = -60
            self.x = random.randint(-40, WIDTH-20)


def main():
    player = User(220, 300, 60, 100, 0, 0)
    cloud1 = Cloud(-100, 100, 60, 3)
    cloud2 = Cloud(-150, 150, 90, 3)
    cloud3 = Cloud(-50, 90, 50, 3)

    run = True
    while run:
        screen.fill(SKY_BLUE)

        cloud1.move()
        cloud1.draw()
        cloud2.move()
        cloud2.draw()
        cloud3.move()
        cloud3.draw()

        player.draw()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        pg.display.update()
        clock.tick(100)
    
    pg.quit()


main()
