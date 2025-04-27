import pygame  as py
import sys
import funciones as fun

# pygame setup
py.init()

screen = py.display.set_mode((fun.height, fun.width), py.RESIZABLE)

py.display.set_caption("juego")

background_original = py.image.load('img1.jpg').convert()

background_juego=fun.size_img(background_original, screen)

screen.blit(background_juego, (0,0))


clock_fps = py.time.Clock()
running = True
dt = 0

player_pos = py.Vector2(screen.get_width() / 4, screen.get_height() / 4)
player_radio= 40

triangle_height= 40
triangle_base= 40

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        elif event.type == py.VIDEORESIZE:
            background_juego= fun.size_img(background_original, screen)


            screen.blit(background_juego, (0, 0))

    punto1= (player_pos.x, player_pos.y - triangle_height / 2)
    punto2= (player_pos.x - triangle_base / 2, player_pos.y + triangle_height / 2)
    punto3= (player_pos.x + triangle_base / 2, player_pos.y + triangle_height / 2)

    
    py.draw.polygon(screen, "blue", [punto1, punto2, punto3])

    keys = py.key.get_pressed()
    if keys[py.K_w]:
        player_pos.y -= 300 * dt
    if keys[py.K_s]:
        player_pos.y += 300 * dt
    if keys[py.K_a]:
        player_pos.x -= 300 * dt
    if keys[py.K_d]:
        player_pos.x += 300 * dt

    screen_rect= screen.get_rect()


    if player_pos.x - triangle_base <screen_rect.left:
        player_pos.x = screen_rect.left + triangle_base

    if player_pos.x + triangle_base > screen_rect.right:
        player_pos.x = screen_rect.right - triangle_base

    if player_pos.y - triangle_height < screen_rect.top:
        player_pos.y = screen_rect.top + triangle_height
    
    if player_pos.y + triangle_height > screen_rect.bottom:
        player_pos.y = screen_rect.bottom - triangle_height 


    # flip() the display to put your work on screen
    py.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock_fps.tick(500) / 1000

py.quit()
sys.exit()