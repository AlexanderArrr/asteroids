import pygame, os
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    os.environ['SDL_VIDEO_WINDOW_POS'] = '1920,0'
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            if ast.check_collision(player):
                print("Game over!")
                return pygame.QUIT

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        dt = (clock.tick(60)) / 1000


if __name__ == "__main__":
    main()