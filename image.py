import pygame, sys
pygame.init ()
screen = pygame.display.set_mode ([640, 480])
screen.fill ([144, 22, 67])
my_ball = pygame.image.load ('Ball.png')
x = 50
y = 50
x_speed = 5
y_speed = 5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit ()

    pygame.time.delay (10)
    pygame.draw.rect (screen,[144, 22, 67], [x, y, 120 , 120], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width () - 110 or y<0:
        x_speed = - x_speed

    if y > screen.get_height () - 110 or y<0:
        y_speed = - y_speed
    screen.blit (my_ball, [x, y])
    pygame.display.flip ()
