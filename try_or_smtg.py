import random

import pygame
from pygame.locals import*
# background_colour = (9, 121, 105)
import pygame
def white_backround():
    # img = pygame.image.load(r'C:\Users\jbt\Desktop\elice_and_rotem_pro\bin\bin\grass.png')
    img=pygame.image.load(r"bin\bin\grass.png")
    IMAGE_SMALL = pygame.transform.scale(img, (60, 40))
    img2 = pygame.image.load(r'bin\bin\flag.png')
    IMAGE_SMALLi = pygame.transform.scale(img2, (80, 60))
    white = ((9, 121, 105))
    BOARD_ROWS = 25
    BOARD_COLS = 50
    CELL_SIZE = 20
    WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
    WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    running = 1


    while running:
        screen.fill((white))
        for i in range(21):
            wigth=random.randint(0,47)*20
            hight=random.randint(0,25)*20
            screen.blit(IMAGE_SMALL,(wigth,hight))
            running=0

    running = 1
    while running:
        screen.blit(IMAGE_SMALLi, ((46 * 20),(22 * 20)))
        pygame.display.flip()


def black_backrount():
    BLACK = (0, 0, 0)
    WHITE = (9, 121, 105)
    BOARD_ROWS = 25
    BOARD_COLS = 50
    CELL_SIZE = 20
    WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
    WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREEN.fill(BLACK)
    img = pygame.image.load(r"bin\bin\mine.png")
    IMAGE_SMALL = pygame.transform.scale(img, (60, 20))
    runing=1
    while True:
        blockSize = 20 #Set the size of the grid block
        for x in range(0, WINDOW_WIDTH, blockSize):
            for y in range(0, WINDOW_HEIGHT, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        while runing:
            for i in range(21):
                hight = random.randint(0, 25) * 20
                if hight>21:
                    wigth = random.randint(0, 45) * 20
                    SCREEN.blit(IMAGE_SMALL, (wigth, hight))
                if hight<=21:
                    wigth = random.randint(0, 47) * 20
                    SCREEN.blit(IMAGE_SMALL, (wigth, hight))
                runing=0

        pygame.display.update()

#black_backrount()
