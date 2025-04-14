import pygame as pyg
import sys
import funciones as fun


pyg.init()
screen = pyg.display.set_mode((fun.heightq, fun.widthq), pyg.RESIZABLE)
pyg.display.set_caption("juego")

background_original= pyg.image.load("img/images.jpg").convert()

background_juego= fun.size_img(background_original, screen)
screen.blit(background_juego, (0,0))

clock_fps = pyg.time.Clock()
running = True

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        elif event.type == pyg.VIDEORESIZE:
            background_juego= fun.size_img(background_juego, screen)
    screen.blit(background_juego (0,0))
    
    pyg.display.flip()
    pyg.display.update()
    clock_fps.tick(60) # limits fps to 60
    
pyg.quit()
sys.exit()

