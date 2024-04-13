import pygame as pg
import sys
import time
from tower import Tower, Piece


pg.init();
pg.display.init()
pg.display.set_mode(size=(1280, 720))
screen = pg.display.get_surface()

rect = pg.Surface(size=(32, 32))
rect.fill((255, 255, 255))

tower = Tower(5, (500, 500))

input_store = []

while True:
    events = pg.event.get()

    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                input_store.append(1)
            if event.key == pg.K_2:
                input_store.append(2)
            if event.key == pg.K_3:
                input_store.append(3)

    if len(input_store) >= 2:
        tower.change(input_store[-2], input_store[-1])
        input_store = []

    screen.fill((0,0,0))

    tower.blit(screen)

    pg.display.update()
    time.sleep(0.001)

