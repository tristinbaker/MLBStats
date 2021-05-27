import pygame
import sys
import time

from application_manager import ApplicationManager
from game import Game
from button import Button

team = sys.argv[1]

app_mgr = ApplicationManager(team)
left_button = Button(app_mgr, 'default', (400, 300), 40, 'Clicked')
right_button = Button(app_mgr, 'default', (500, 300), 40, 'Clicked')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		left_button.click(event)
		right_button.click(event)
	left_button.show()
	right_button.show()
	game = Game(app_mgr)
	pygame.display.flip()
	games = game.get_games()
	braves_game = game.get_main_game(games)
	left_game = game.get_left_game(games, braves_game['id'])
	right_game = game.get_right_game(games)
	left_button = Button(app_mgr, left_game['shortName'], (230, 455), 40, 'Clicked')
	right_button = Button(app_mgr, right_game['shortName'], (420, 455), 40, 'Clicked')
	app_mgr.draw_game(braves_game)
	#time.sleep(1)
