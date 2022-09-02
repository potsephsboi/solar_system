from helper import *



pygame.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_win():
    WIN.fill(WHITE)
    for p in Planet.Planets:
        WIN.blit(p.icon, ((p.pos[0]-(p.size[0]/2)), p.pos[1]-(p.size[1]/2)))

    pygame.display.update()

def move_planets(PL=Planet.Planets):
    for p in PL:
        if p.name != 'sun':
            p.pos[0] += p.vx
            p.pos[1] += p.vy

def update_vel(dt, PL=Planet.Planets):
    for p in PL:
        if p.name != 'sun':
            p.vx = p.vmax * math.cos(p.ang_vel * dt)
            p.vy = p.vmax * math.sin(p.ang_vel * dt)

def main():
    s_time = time.time()
    clock = pygame.time.Clock()
    run = True
    pause = False
    relocate_planets = False
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                pause = not pause
                relocate_planets = not relocate_planets


        if not pause:
            draw_win()
            update_vel(time.time()-s_time)
            move_planets()        

        if relocate_planets:        
            s_time = time.time()
            Planet.Planets.clear()
            init_planets()
            relocate_planets = not relocate_planets
             
if __name__ == '__main__':
    init_planets()
    main()
