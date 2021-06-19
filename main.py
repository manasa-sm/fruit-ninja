import pygame
import os

pygame.font.init()

WIDTH, HEIGHT = 900, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.display.set_caption("Fruit Ninja")

BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets','background.jpg')), (WIDTH, HEIGHT))

GAME_FONT = pygame.font.SysFont('comicsans',30)

button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2  + 60, 200, 50)

def draw_window():
    WIN.blit(BACKGROUND, (0,0))
    pygame.display.update()

def draw_splash_screen():
    WIN.blit(BACKGROUND, (0,0))
    pygame.draw.rect(WIN, WHITE, button)
    start_game_text = GAME_FONT.render("Start Game", 1, BLACK)
    WIN.blit(start_game_text, (WIDTH//2 - 60, HEIGHT//2 + 75))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_splash_screen()
    pygame.quit()

if __name__ == "__main__":
    main()