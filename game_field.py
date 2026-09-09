from tkinter.constants import BROWSE

import consts
import random
import math

matrix = consts.matrix


def spot_list():
    i = 0
    spot_list = []
    while i < 21:
        wigth = random.randint(0, 47)*20
        hight = random.randint(0, 24)*20
        spot_list.append((wigth, hight))
        i = i + 1
    return spot_list


grass_list = spot_list()

for item in grass_list:
    matrix[item[1]//20][item[0]//20] = 'Grass'
    matrix[item[1] // 20][(item[0] // 20)-1] = 'Grass'
    matrix[item[1]//20][(item[0]//20)+1] = 'Grass'
    # matrix[3][7]="G"

bomb_list = spot_list()

for item in bomb_list:
    matrix[item[1]//20][item[0]//20] = 'BOMB'
    matrix[item[1] // 20][(item[0] // 20) - 1] = 'BOMB'
    matrix[item[1] // 20][(item[0] // 20) + 1] = 'BOMB'


# for line in matrix:
# print(line)


def is_touched_bomb(x, y):

    min_dist = 100000
    min_row = -1
    min_col = -1
    row_count = -1
    # print(grass_list)

    for row in matrix:
        row_count = row_count + 1
        col_count = -1
        for col in row:
            col_count = col_count + 1
            pos_list = [row_count, col_count]
            pos_player_list = [(y / 20) + 3, (x / 20)]
            # print(pos_player_list)

            dist = math.dist(pos_list, pos_player_list)

            if min_dist > dist:
                min_dist = dist
                min_row = row_count-1
                min_col = col_count
    #
    # print(min_row, min_col)
    # if (min_row,min_col) in grass_list:
    print(min_row,min_col)
    if matrix[min_row][min_col] == "Grass" or matrix[min_row][min_col + 1] == "G" or matrix[min_row][min_col -1] == "G":
        return True
        # elif min_row<24 min_col<48:
        # if matrix[min_row][min_col+1] == "G":
        return True
    else:
        return False


def is_touched_flag():
    pass


