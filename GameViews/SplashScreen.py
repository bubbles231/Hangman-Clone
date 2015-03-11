# coding=utf-8
"""
This will be my SplashScreen file.
"""
from Engine.ResourceLoader import *


class SplashScreen():
    """
    Run the SplashScreen of the game.
    """

    def __init__(self, gm):
        self.splash, self.splash_rect = ResourceLoader().load_image(
            'Splash1.png')
        self.sound = ResourceLoader().load_sound('Splash_Sound1.wav')
        self.button_one = ResourceLoader().make_button(gm, (110, 140, 35),
                                                       200, 320,
                                                       200, 100, 0, "Click"
                                                                    "Me!",
                                                       (255, 255, 255))

    def get_input(self, gm):
        """
        :param gm: gm = GameManager Class
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gm.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_one.pressed(pygame.mouse.get_pos()):
                    print("Give me a command!")
                    self.sound.play()
                    print("Make Main Menu!")

    def recalculate(self, gm):
        """

        :param gm:  gm = GameManager Class
        """
        pass

    def render(self, gm):
        """

        :param gm: gm = GameManager Class
        """
        gm.screen.blit(self.splash, self.splash_rect)
        self.button_one.draw_button(gm.screen)
        pygame.display.flip()
