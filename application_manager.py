import pygame
import io
from settings import *
from button import Button
try:
    # Python2
    from urllib2 import urlopen
except ImportError:
    # Python3
    from urllib.request import urlopen

class ApplicationManager:

	def __init__(self, team):
		pygame.init()
		pygame.display.set_mode([800, 480])
		pygame.display.set_caption("Braves Tracker")
		self.SURFACE = pygame.display.get_surface()
		self.score_font = pygame.font.SysFont('font.ttf', 72)
		self.stat_font = pygame.font.SysFont('font.ttf', 24)
		self.background = WHITE
		self.team = team

	def draw_game(self, game):
		home_score = game['competitions'][0]['competitors'][0]['score']
		home_team = game['competitions'][0]['competitors'][0]['team']['abbreviation']
		home_record = game['competitions'][0]['competitors'][0]['records'][0]['summary']
		away_score = game['competitions'][0]['competitors'][1]['score']
		away_team = game['competitions'][0]['competitors'][1]['team']['abbreviation']
		away_record = game['competitions'][0]['competitors'][1]['records'][0]['summary']
		inning = game['status']['type']['detail']
		try:
			pitcher = game['competitions'][0]['situation']['pitcher']['athlete']['fullName']
			pitcher_headshot = game['competitions'][0]['situation']['pitcher']['athlete']['headshot']
			pitcher_stats = game['competitions'][0]['situation']['pitcher']['summary']
			batter = game['competitions'][0]['situation']['batter']['athlete']['fullName']
			batter_headshot = game['competitions'][0]['situation']['batter']['athlete']['headshot']
			batter_stats = game['competitions'][0]['situation']['batter']['summary']
			outs = game['competitions'][0]['situation']['outs']
			balls = str(game['competitions'][0]['situation']['balls'])
			strikes = str(game['competitions'][0]['situation']['strikes'])
		except KeyError:
			self.SURFACE.fill(self.background)
			dash = pygame.draw.line(self.SURFACE, BLACK, (380, 85), (400, 85))
			home_team_img = pygame.image.load(f"teams/{home_team}.png")
			home_team_img = pygame.transform.scale(home_team_img, eval(f"{home_team}_SIZE"))
			home_score_img = self.score_font.render(str(home_score), True, BLACK)
			home_record_text = self.stat_font.render(home_record, True, BLACK)
			self.SURFACE.blit(home_team_img, (180,20))
			self.SURFACE.blit(home_score_img, (310,60))
			self.SURFACE.blit(home_record_text, (215, 140))

			away_team_img = pygame.image.load(f"teams/{away_team}.png")
			away_team_img = pygame.transform.scale(away_team_img, eval(f"{away_team}_SIZE"))
			away_team_score = self.score_font.render(str(away_score), True, BLACK)
			away_record_text = self.stat_font.render(away_record, True, BLACK)
			self.SURFACE.blit(away_team_img, (490, 20))
			self.SURFACE.blit(away_team_score, (440,60))
			self.SURFACE.blit(away_record_text, (525, 140))

			inning_text = self.score_font.render(inning, True, BLACK)
			inning_location = (330, 250) if inning == 'Final' else (290, 250)
			self.SURFACE.blit(inning_text, inning_location)
			return False

		self.SURFACE.fill(self.background)
		inning_dash = pygame.draw.line(self.SURFACE, BLACK, (380, 85), (400, 85))
		self.draw_base_status(game['competitions'][0]['situation'])

		inning_text = self.stat_font.render(inning, True, BLACK)
		inning_location = (350, 150) if inning.split(' ')[0] == 'Bottom' else (360, 150)
		if inning.split(' ')[0] == 'Rain':
			inning_location = (310, 150)
		self.SURFACE.blit(inning_text, inning_location)

		balls_text = self.stat_font.render(balls, True, BLACK)
		strikes_text = self.stat_font.render(strikes, True, BLACK)
		self.SURFACE.blit(balls_text, (369, 175))
		self.SURFACE.blit(strikes_text, (398, 175))
		self.ball_strikes_dash = pygame.draw.line(self.SURFACE, BLACK, (382, 180), (392, 180))
		self.draw_outs(outs)

		home_team_img = pygame.image.load(f"teams/{home_team}.png")
		home_team_img = pygame.transform.scale(home_team_img, eval(f"{home_team}_SIZE"))
		home_score_img = self.score_font.render(str(home_score), True, BLACK)
		home_record_text = self.stat_font.render(home_record, True, BLACK)
		self.SURFACE.blit(home_team_img, (180,20))
		self.SURFACE.blit(home_score_img, (310,60))
		self.SURFACE.blit(home_record_text, (215, 140))

		away_team_img = pygame.image.load(f"teams/{away_team}.png")
		away_team_img = pygame.transform.scale(away_team_img, eval(f"{away_team}_SIZE"))
		away_team_score = self.score_font.render(str(away_score), True, BLACK)
		away_record_text = self.stat_font.render(away_record, True, BLACK)
		self.SURFACE.blit(away_team_img, (490, 20))
		self.SURFACE.blit(away_team_score, (440,60))
		self.SURFACE.blit(away_record_text, (525, 140))

		pitcher_img_str = urlopen(pitcher_headshot).read()
		pitcher_img_bytes = io.BytesIO(pitcher_img_str)
		pitcher_img = pygame.image.load(pitcher_img_bytes)
		pitcher_img = pygame.transform.scale(pitcher_img, (120,85))
		pitcher_location = (170,220) if inning.split(' ')[0] == 'Top' else (490, 220)
		pitcher_stat_location = (155, 320) if inning.split(' ')[0] == 'Top' else (475, 320)
		pitcher_stat_text = self.stat_font.render(pitcher_stats, True, BLACK)
		pitcher_name = self.stat_font.render(pitcher, True, BLACK)
		pitcher_name_location = (170, 200) if inning.split(' ')[0] == 'Top' else (490,200)
		self.SURFACE.blit(pitcher_img, pitcher_location)
		self.SURFACE.blit(pitcher_stat_text, pitcher_stat_location)
		self.SURFACE.blit(pitcher_name, pitcher_name_location)
		
		batter_img_str = urlopen(batter_headshot).read()
		batter_img_bytes = io.BytesIO(batter_img_str)
		batter_img = pygame.image.load(batter_img_bytes)
		batter_img = pygame.transform.scale(batter_img, (120,85))
		batter_location = (490,220) if inning.split(' ')[0] == 'Top' else (170,220)
		batter_stat_location = (500, 320) if inning.split(' ')[0] == 'Top' else (160, 320)
		batter_stat_text = self.stat_font.render(batter_stats, True, BLACK)
		batter_name = self.stat_font.render(batter, True, BLACK)
		batter_name_location = (490, 200) if inning.split(' ')[0] == 'Top' else (170,200)
		self.SURFACE.blit(batter_img, batter_location)
		self.SURFACE.blit(batter_stat_text, batter_stat_location)
		self.SURFACE.blit(batter_name, batter_name_location)

	def draw_base_status(self, situations):
		thirdRect = [(365, 250), (375, 240), (385, 250), (375, 260)]
		secondRect = [(380, 230), (390, 220), (400, 230), (390, 240)]
		firstRect = [(395,250), (405, 240), (415, 250), (405, 260)]
		if(situations['onFirst']):
			if(situations['onSecond']):
				if(situations['onThird']):
					pygame.draw.polygon(self.SURFACE, YELLOW, thirdRect)
					pygame.draw.polygon(self.SURFACE, YELLOW, secondRect)
					pygame.draw.polygon(self.SURFACE, YELLOW, firstRect)
				else:
					pygame.draw.polygon(self.SURFACE, BLACK, thirdRect, 1)
					pygame.draw.polygon(self.SURFACE, YELLOW, secondRect)
					pygame.draw.polygon(self.SURFACE, YELLOW, firstRect)
			else:
				pygame.draw.polygon(self.SURFACE, BLACK, thirdRect, 1)
				pygame.draw.polygon(self.SURFACE, BLACK, secondRect, 1)
				pygame.draw.polygon(self.SURFACE, YELLOW, firstRect)
		elif(situations['onSecond']):
			if(situations['onThird']):
				pygame.draw.polygon(self.SURFACE, YELLOW, thirdRect)
				pygame.draw.polygon(self.SURFACE, YELLOW, secondRect)
				pygame.draw.polygon(self.SURFACE, BLACK, firstRect, 1)
			else:
				pygame.draw.polygon(self.SURFACE, BLACK, thirdRect, 1)
				pygame.draw.polygon(self.SURFACE, YELLOW, secondRect)
				pygame.draw.polygon(self.SURFACE, BLACK, firstRect, 1)
		elif(situations['onThird']):
			pygame.draw.polygon(self.SURFACE, YELLOW, thirdRect)
			pygame.draw.polygon(self.SURFACE, BLACK, secondRect, 1)
			pygame.draw.polygon(self.SURFACE, BLACK, firstRect, 1)
		else:
			pygame.draw.polygon(self.SURFACE, BLACK, thirdRect, 1)
			pygame.draw.polygon(self.SURFACE, BLACK, secondRect, 1)
			pygame.draw.polygon(self.SURFACE, BLACK, firstRect, 1)

	def draw_outs(self, outs):
		if(outs == 0):
			pygame.draw.circle(self.SURFACE, BLACK, (373, 200), 5, 2)
			pygame.draw.circle(self.SURFACE, BLACK, (403, 200), 5, 2)
		elif(outs == 1):
			pygame.draw.circle(self.SURFACE, BLACK, (373, 200), 5)
			pygame.draw.circle(self.SURFACE, BLACK, (403, 200), 5, 2)
		elif(outs == 2):
			pygame.draw.circle(self.SURFACE, BLACK, (373, 200), 5)
			pygame.draw.circle(self.SURFACE, BLACK, (403, 200), 5)

	def change_team(self, team):
		self.team = team