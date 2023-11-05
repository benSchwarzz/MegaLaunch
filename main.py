import pygame as pg
import random, math
import pygame.freetype
pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)
font = pygame.freetype.Font(None, 20)

WIDTH, HEIGHT = 500, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))

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
        self.sprite1 = pg.image.load("pixil-frame-0 (6).png")
        self.sprite2 = pg.image.load("pixil-frame-0 (7).png")
        self.current_sprite = self.sprite2
        self.powered = False

    def draw(self, left, right):
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
            

    
class Cloud:
    def __init__(self, x, dy):
        self.x = x
        self.y = -50
        self.width = 100
        self.height = 50
        self.dy = dy
        self.sprite = pg.image.load("pixil-frame-0 (8).png")
        
    
    def draw(self):
        self.box = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.sprite, self.box)

        self.y += self.dy

        

class Fuel:
    def __init__(self, x, dy):
        self.width = 25
        self.height = 41
        self.x = x
        self.y = -42
        self.dy = dy
        self.image = pg.image.load("pixil-frame-0 (9).png")
        self.sprite = pg.transform.scale(self.image, (25, 41))
    
    def draw(self):
        self.hit_box = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.sprite, self.hit_box)

        self.y += self.dy



def main():
    player = User(220, 300, 60, 100, -10, 0, 0.07)
    last_time: int = pg.time.get_ticks()
    last_time1: int = pg.time.get_ticks()
    sprite_time: int = 0
    initial_time = pg.time.get_ticks()
    elapsed_time: int = 0
    fuel_range: list = [400, 1000]
    altitude = 0


    fuels = []
    clouds = []

    run = True
    while run:
        
        elapsed_time = pg.time.get_ticks() - initial_time
        screen.fill(SKY_BLUE)

        if player.y > HEIGHT + 20:
            run = False

        if elapsed_time > 10000:
            pass

        new_time1: int = pg.time.get_ticks()
        if (new_time1 - last_time1) > random.randint(400, 1200):
            last_time1 = pg.time.get_ticks()
            
            cloud = Cloud(random.randint(0, WIDTH-25), -20)
            clouds.append(cloud)

        for c in clouds:
            if player.dy < 0:
                c.dy = -1*player.dy
            else:
                c.dy = 0
            
            if c.y > HEIGHT+2:
                clouds.remove(c)
            c.draw()

        new_time: int = pg.time.get_ticks()
        if (new_time - last_time) > random.randint(fuel_range[0], fuel_range[1]):
            last_time = pg.time.get_ticks()
            
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

        try:
            for f in fuels:
                if f.hit_box.colliderect(player.hit_box):
                    fuels.remove(f)
                    sprite_time = elapsed_time
                    player.powered = True
                    player.dy -= 6
        except:
            pass

        if (elapsed_time - sprite_time) > 1000:
            player.powered = False


        player.draw(pg.K_a, pg.K_d)

        altitude += int((-1*player.dy*elapsed_time)/1000)
        font.render_to(screen, (10, 10), f"Altitude: {altitude}m", BLACK)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        pg.display.update()
        clock.tick(100)
    
    pg.quit()


main()
