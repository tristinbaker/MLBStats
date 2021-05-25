from datetime import date
import requests

class Game: 

	def __init__(self):
		self.today = date.today()
		self.today.strftime("%Y-%m-%d")

		self.url = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/scoreboard"

	def get_braves_game(self):
		response = requests.get(self.url)
		games = response.json()['events']
		for game in games:
			home_team = game['competitions'][0]['competitors'][0]['team']['abbreviation']
			if home_team == 'OAK':
				braves_game = game
				return braves_game