# Importing pygame module
import pygame
from pygame.locals import *
import random


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
i = 0
spot_list=[]
while i<21:
   wigth = random.randint(0, 47) * 20
   hight = random.randint(0, 25) * 20
   spot_list.append((wigth,hight))
   i = i + 1
print(spot_list)
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


   window.blit(IMAGE_SMALLi, ((46 * 20),(22 * 20)))




   # iterate over the list of Event objects
   # that was returned by pygame.event.get() method.
   for event in pygame.event.get():


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
   if key_pressed_is[K_RIGHT]:
       x += 2
   if key_pressed_is[K_UP]:
       y -= 2
   if key_pressed_is[K_DOWN]:
       y += 2


   # print(x/20,y/20)


   # Draws the surface object to the screen.
   pygame.display.update()

