import pygame
from asteroidfield import AsteroidField
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
def main():
	dt = 0.0
	clock = pygame.time.Clock()
	pygame.init()
	print("Starting Asteroids")
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containters = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	hero = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = clock.tick(60) / 1000
		updatable.update(dt)
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		updatable
		pygame.display.flip()
if __name__ == "__main__":
    main()
