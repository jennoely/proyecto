import pygame as pyg
heightq, widthq = 720, 480 

font_large= pyg.font.SysFont("arial", 36)
def size_img(background_original, screen):
    ventana=screen.get_size()
    return pyg.transform.scale(background_original, ventana)