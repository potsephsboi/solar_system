import pygame 


WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_win():
    WIN.fill(WHITE)
    pygame.display.update()


def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        draw_win()


if __name__ == '__main__':
    main()
