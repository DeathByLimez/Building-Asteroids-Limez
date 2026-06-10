import pygame
import sys
from asteroidfield import AsteroidField
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from logger import log_event
from shot import Shot
def main():
    dt = 0.0
    clock = pygame.time.Clock()
    pygame.init()
    print("Starting Asteroids")
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, drawable, updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    hero = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        updatable.update(dt)
                        if asteroid.collides_with(shots)
                for asteroid in asteroids:
                        if asteroid.collides_with(hero):
                                log_event("player_hit")
                                print("Game over!")
                                sys.exit()
                for s in shots:
                        if asteroid.collides_with(s):
                                log_event("asteroid_shot")
                                s.kill()
                                        asteroid.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
if __name__ == "__main__":
    main()
