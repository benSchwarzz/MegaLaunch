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

    def draw(self, left, right):
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.current_sprite, self.hit_box)
        keys = pg.key.get_pressed()
        powered = False

        ### y direction
        if not powered:
            self.dy += 0.5
            
            if self.y < 300:
                self.y = 300

            if self.dy < 0:
                if self.y > 300:
                    self.y += self.dy
            elif self.dy > 0:
                if self.y > HEIGHT-self.height:
                    self.y += self.dy
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

class Fuel:
    def __init__(self, x, dy):
        self.width = 25
        self.height = 41
        self.x = x
        self.y = -42
        self.dy = dy
        self.image = pg.image.load("SpaceShip Adventure/images/pixil-frame-0 (9).png")
        self.sprite = pg.transform.scale(self.image, (25, 41))
    
    def draw(self):
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.sprite, self.hit_box)

        self.y += self.dy



def main():
    player = User(220, 300, 60, 100, -10, 0)
    last_time: int = pg.time.get_ticks()

    fuels = []

    run = True
    while run:
        screen.fill(SKY_BLUE)

        new_time: int = pg.time.get_ticks()
        if (new_time - last_time) > random.randint(1000, 4000):
            last_time = pg.time.get_ticks()

            print("created")

            fuel = Fuel(random.randint(0, WIDTH-25), -20)
            
            fuels.append(fuel)

        for f in fuels:
            if player.dy < 0:
                f.dy = -1*player.dy
            else:
                f.dy = 0
            
            if f.y > HEIGHT+2:
                fuels.remove(f)
            f.draw()

        player.draw(pg.K_a, pg.K_d)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        pg.display.update()
        clock.tick(100)
    
    pg.quit()


main()
