from helper import *


WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)

pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_win():
    WIN.fill(WHITE)
    for p in Planet.Planets:
        WIN.blit(p.icon, ((p.pos[0]-(p.size[0]/2)), p.pos[1]-(p.size[1]/2)))
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
