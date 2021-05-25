import pygame
import sys
import time

from application_manager import ApplicationManager
from game import Game

app_mgr = ApplicationManager()
game = Game()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.flip()
	braves_game = game.get_braves_game()
	app_mgr.draw_braves_game(braves_game)
	#time.sleep(1)
