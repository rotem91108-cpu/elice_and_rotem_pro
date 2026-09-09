# consts.py
from annotationlib import Format
from argparse import ArgumentDefaultsHelpFormatter
from shutil import SameFileError
import random


BOARD_ROWS = 25
BOARD_COL = 50
FLAG_ROWS = 3

BOARD_LENGTH = 1000
BOARD_HIGTH = 500
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3
SOLDIER_FEET_ROWS = 1
SAFE = 'S'

game_board = []

matrix = [ [ SAFE for i in range(BOARD_COL) ] for j in range(BOARD_ROWS) ]






