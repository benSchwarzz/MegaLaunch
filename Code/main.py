import pygame as pg
import random, math
import pygame.freetype
from Classes.user import User
from Classes.fuels import Fuel
from Classes.clouds import Cloud
from Classes.powerups import Speed_boost


pg.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
init_R, init_G, init_B = 120, 200, 255
SKY_BLUE = init_R, init_G, init_B
font = pygame.freetype.Font(None, 20)

WIDTH, HEIGHT = 500, 700
screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()

def main():
    player = User(220, 300, 60, 100, -10, 0, 0.07)
    sprite_time: int = 0
    last_time = pg.time.get_ticks()
    last_time1 = pg.time.get_ticks()
    last_time2 = pg.time.get_ticks()
    initial_time = pg.time.get_ticks()
    elapsed_time: int = 0
    fuel_range: list = [400, 1000]
    altitude = 0

    fuels = []
    clouds = []
    powerups = []

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
            c.draw(screen)

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
            f.draw(screen)

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
            
        new_time2: int = pg.time.get_ticks()
        if (new_time2 - last_time2) > random.randint(10000, 20000):
            last_time2 = pg.time.get_ticks()
            
            powerup = Speed_boost(random.randint(0, WIDTH-25), -20)
            powerups.append(powerup)

        for p in powerups:
            if player.dy < 0:
                p.dy = -1*player.dy
            else:
                p.dy = 0
            
            if p.y > HEIGHT+2:
                powerups.remove(p)
            p.draw(screen)

        for p in powerups:
            if p.hit_box.colliderect(player.hit_box):
                player.dy -= 20
                player.powered = True
                sprite_time = elapsed_time
                powerups.remove(p)


        player.draw(screen, pg.K_a, pg.K_d)

        altitude += int((-1*player.dy*elapsed_time)/1000)
        font.render_to(screen, (10, 10), f"Altitude: {altitude}m", BLACK)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        
        pg.display.update()
        clock.tick(100)
    
    pg.quit()


main()

