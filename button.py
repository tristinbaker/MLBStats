from settings import *
import pygame

class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, app_mgr, text, pos, font_size, feedback=""):
        self.x, self.y = pos
        self.app_mgr = app_mgr
        self.font = pygame.font.SysFont("font.ttf", font_size)
        self.bg = NAVY
        self.game = text
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(self.game)
 
    def change_text(self, text):
        """Change the text whe you click"""
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(self.bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0] + 50, self.size[1] + 50)
 
    def show(self):
        self.app_mgr.SURFACE.blit(self.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    print('mouse clicked')
                    self.app_mgr.change_team((self.game[0:3]).rstrip())