import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Ninja")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets','background.png')), (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(BACKGROUND, (0,0))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()