import pygame
import random

#tiles
def tile(x, y):
    return x * 32, y * 32

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole = 0,0
        width= 20
        height= 16

        while running:


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #mouse click
                    mouse = event.pos

                    # mole / mouse tile radius
                    if  mole[0] * 32 <= mouse[0] <=  mole[0] * 32 + 32 and mole[1] * 32 <= mouse[1] <= mole[1] * 32 + 32:
                        #reset mole after
                        mole = random.randrange(0,width), random.randrange(0,height)

                elif event.type == pygame.QUIT:
                    running = False

            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(tile(mole[0], mole[1]))))

            #lines
            for line in range(width):
                pygame.draw.line(screen, "dark green", (32 * line, 0), (32 * line, 512))

            for line in range(height):
                pygame.draw.line(screen, "dark green", (0, 32 * line), (640, 32 * line))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()




if __name__ == "__main__":
    main()
