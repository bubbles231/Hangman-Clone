# coding=utf-8
"""
This will be my SplashScreen file.
"""
from Engine.ResourceLoader import *

class SplashScreen():
    """
    Run the SplashScreen of the game.
    """

    def __init__(self):
        self.splash, self.splash_rect = ResourceLoader().load_image(
            'Splash1.png')
        self.sound = ResourceLoader().load_sound('Splash_Sound1.wav')

    def get_input(self, GM):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GM.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sound.play()
                print("Make Main Menu!")
                GM.current_screen = self


    def recalculate(self, GM):
        pass

    def render(self, GM):
        GM.screen.blit(self.splash, self.splash_rect)
        pygame.display.flip()
