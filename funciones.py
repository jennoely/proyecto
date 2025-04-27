import pygame as py
height, width = 720, 480 

def size_img(background_original, screen):
    ventana = screen.get_size()
return py.transform.scale(background_original, ventana)