"""
This is the game manager class.
Arthur Marble
"""
# coding=utf-8
import os
import pygame
from GameViews.SplashScreen import SplashScreen


class GameManager:

    """
    GameManager Class
    """

    def __init__(self):
        pygame.init()
        # TODO: Make a menu where I modify the screen
        self.screen_length = 640
        self.screen_width = 400
        self.screen = pygame.display.set_mode((self.screen_length,
                                               self.screen_width))
        pygame.display.set_caption("Hangman Clone!")
        self.playing = True
        self.current_screen = SplashScreen()
        self.previous_screen = None

    def get_input(self):
        self.current_screen.get_input(self)

    def recalculate(self):
        self.current_screen.recalculate(self)

    def render(self):
        self.current_screen.render(self)

    def run_game_loop(self):
        while self.playing:
            # Handle input
            self.get_input()

            # Logic handling
            self.recalculate()

            # Render screen
            self.render()

            pygame.time.Clock().tick(60)  # TODO: Make fps adjustable in setting
