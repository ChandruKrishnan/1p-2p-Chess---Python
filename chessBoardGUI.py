import pygame
import sys

pygame.init()

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
square_size = width // 8

WHITE, BLACK = (255,255,255), (0,0,0)

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("1 Player Chess Game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for row in range(8):
        for column in range(8):
            color = WHITE if (row + column) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (column * square_size, row * square_size, square_size, square_size))
    pygame.display.flip()