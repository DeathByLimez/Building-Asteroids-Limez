import pygame

from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
	dt = 0.0
	Clock = pygame.time.Clock()
	pygame.init()
	print("Starting Asteroids")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	hero = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		dt = Clock.tick(60) / 1000
		hero.update(dt)
		screen.fill("black")
		hero.draw(screen)
		pygame.display.flip()
if __name__ == "__main__":
    main()
