
import pygame

from logger import log_state

from constants import SCREEN_WIDTH

from constants import SCREEN_HEIGHT
def main():
	dt = 0.0
	pygame.time.clock()
	



	pygame.init()
	print("Starting Asteroids")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			dt = clock.tick(60) / 1000
			print(f"{dt}")
		screen.fill("black")
		pygame.display.flip()
if __name__ == "__main__":
    main()
