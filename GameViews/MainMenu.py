# coding=utf-8
"""
This will be my MainMenu file.
"""
from Engine.ResourceLoader import *


class MainMenu():
    """
    Run the MainMenu of game.
    """

    def __init__(self, gm):
        self.bg = pygame.Surface((gm.screen_height, gm.screen_width))
        self.bg_rect = self.bg.get_rect()
        print("self.bg_rect:", self.bg_rect)
        self.bg_color = ((100, 140, 50))
        self.bg.fill(self.bg_color)
        gm.screen.blit(self.bg, self.bg_rect)

    def get_input(self, gm):
        """
        :param gm: gm = GameManager Class
        :return: None
        """
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and
                    event.key == pygame.K_ESCAPE):
                gm.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                gm.playing = False

    def recalculate(self, gm):
        pass

    def render(self, gm):
        gm.screen.blit(self.bg, self.bg_rect)
        pygame.display.flip()