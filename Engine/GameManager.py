# coding=utf-8
"""
__Arthur Marble__
This is the game manager class. It includes the main game loop and runs until
the program ends. It is a parent class to GameView classes.
"""
import pygame
from . import ResourceLoader


class GameManager:
    """

    GameManager Class
    """

    def __init__(self):
        pygame.init()
        self.fullscreen = False
        self.screen_width = 640
        self.screen_height = 400
        self.fps = 60
        self.playing = True
        self.caption = "Hangman Clone!"
        self.sample_rate = 8000  # This should remain at 8000.
        self.screen = pygame.display.set_mode((self.screen_width,
                                               self.screen_height),
                                              pygame.RESIZABLE)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.caption)
        pygame.mixer.init(self.sample_rate)  # All sound effects will have this sample rate
        #  Hardcoded to SplashScreen because that is how the game is designed to
        #  start. If you want another GameView class make your own set or modify
        #  my code.
        self.resource_loader = ResourceLoader()
        self.current_screen = self.resource_loader.load_class('splash screen',
                                                              self)
        self.previous_screen = None

    def get_input(self):
        """

        Handle Input
        """
        self.current_screen.get_input(self)

    def recalculate(self):
        """

        Handle Logic
        """
        self.screen_rect = self.screen.get_rect()
        self.current_screen.recalculate(self)

    def render(self):
        """

        Render Screen
        """
        self.current_screen.render(self)

    def run_game_loop(self):
        """

        Game loop
        This runs forever until self.playing is equal to false or when
        self.current_screen = None (Would cause crash/not clean exit atm.)
        """
        while self.playing:
            # Handle input
            self.get_input()

            # Logic handling
            self.recalculate()

            # Render screen
            self.render()

            pygame.time.Clock().tick(self.fps)
        else:
            pygame.quit()
