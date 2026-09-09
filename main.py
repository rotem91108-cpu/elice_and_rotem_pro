# Importing pygame module
import pygame
from pygame.locals import *
import random
import consts
import game_field
import screen

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((1000, 500))

# Add caption in the window
pygame.display.set_caption('Player Movement')

# Initializing the clock
# Clocks are used to track and
# control the frame-rate of a game
clock = pygame.time.Clock()

# Add player sprite
img = pygame.image.load(
        r'C:\Users\jbt\Desktop\elice_and_rotem_pro\bin\bin\soldier.png')
image = pygame.transform.scale(img, (40, 60))
img3 = pygame.image.load(r'bin\bin\flag.png')
IMAGE_SMALLi = pygame.transform.scale(img3, (80, 60))

# Store the initial
# coordinates of the player in
# two variables i.e. x and y.
x = 0
y = 0

# Create a variable to store the
# velocity of player's movement
velocity = 200

# Creating an Infinite loop
window.fill((9, 121, 105))

# Display the player sprite at x
# and y coordinates
window.blit(image, (x, y))
img2 = pygame.image.load(r"bin\bin\grass.png")
IMAGE_SMALL2 = pygame.transform.scale(img2, (60, 20))
running = 1

spot_list = game_field.grass_list

run = True
while run:

    # Set the frame rates to 60 fps
    clock.tick(60)

    # Filling the background with
    # white color
    window.fill((9, 121, 105))
    #
    # # Display the player sprite at x
    # # and y coordinates
    window.blit(image, (x, y))
    img2 = pygame.image.load(r"bin\bin\grass.png")
    IMAGE_SMALL2 = pygame.transform.scale(img2, (60, 20))
    for item in spot_list:
        window.blit(IMAGE_SMALL2, item)

    window.blit(IMAGE_SMALLi, ((46 * 20), (21 * 20)))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        # Set the frame rates to 60 fps

        # Filling the background with
        # white color
        window.fill((9, 121, 105))
        #
        # # Display the player sprite at x
        # # and y coordinates
        window.blit(image, (x, y))
        img2 = pygame.image.load(r"bin\bin\grass.png")
        IMAGE_SMALL2 = pygame.transform.scale(img2, (60, 20))
        for item in spot_list:
            window.blit(IMAGE_SMALL2, item)

        window.blit(IMAGE_SMALLi, ((46 * 20), (21 * 20)))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
            screen.black_backrount()

    # Closing the window and program if the
    # type of the event is QUIT
    if event.type == pygame.QUIT:
        run = False
        pygame.quit()
        quit()

# Storing the key pressed in a
# new variable using key.get_pressed()
# method
key_pressed_is = pygame.key.get_pressed()

# Changing the coordinates
# of the player
if key_pressed_is[K_LEFT]:
    x -= 2
    game_field.is_touched_bomb(x, y)
    print(game_field.is_touched_bomb(x, y))
if key_pressed_is[K_RIGHT]:
    x += 2
    game_field.is_touched_bomb(x, y)
    print(game_field.is_touched_bomb(x, y))
if key_pressed_is[K_UP]:
    y -= 2
    game_field.is_touched_bomb(x, y)
    print(game_field.is_touched_bomb(x, y))
if key_pressed_is[K_DOWN]:
    y += 2
    game_field.is_touched_bomb(x, y)
    print(game_field.is_touched_bomb(x, y))
# print(f"{x, y} player c ord")
# print(game_field.is_touched_bomb(x, y))
# print(x,y)

# Draws the surface object to the screen.
pygame.display.update()
