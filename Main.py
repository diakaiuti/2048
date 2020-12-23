import pygame
import sys

from GameFieldDesign import GREEN, PINK
from MainLogic import *

BLOCKS = 4

mas = [BLOCKS][BLOCKS]

SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)

mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 для друзей")

while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, PINK, TITLE_REC)
            pygame.image
            for row in range(BLOCKS):
                for column in range(BLOCKS):
                    w = column * SIZE_BLOCK + (column + 1) * MARGIN
                    h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
                    pygame.draw.rect(screen, GREEN, (w, h, SIZE_BLOCK, SIZE_BLOCK))
            # input()
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas[x][y] = insert_2_or_4()
            print(f'Мы заполнили элемент под номером {random_num}')
            pretty_print(mas)
    pygame.display.update()
