from datetime import date
import requests

class Game: 

	def __init__(self, app_mgr):
		self.today = date.today()
		self.today.strftime("%Y-%m-%d")
		self.app_mgr = app_mgr

		self.url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

	def get_games(self):
		response = requests.get(self.url)
		games = response.json()['events']
		return games

	def get_main_game(self, games):
		for game in games:
			home_team = game['competitions'][0]['competitors'][0]['team']['abbreviation']
			away_team = game['competitions'][0]['competitors'][1]['team']['abbreviation']
			if home_team == self.app_mgr.team or away_team == self.app_mgr.team:
				self.game = game
				return game

	def get_left_game(self, games, brave):
		for i in range(len(games)):
			if games[i]['id'] == self.game['id']:
				if i == 0: 
					return games[len(games) - 1]
				else:
					return games[i-1]

	def get_right_game(self, games):
		for i in range(len(games)):
			if games[i]['id'] == self.game['id']:
				if i == len(games) - 1:
					return games[0]
				else:
					return games[i+1]
