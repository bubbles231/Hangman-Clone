# coding=utf-8
"""
__Arthur Marble__
This will be my SplashScreen for the game.
"""
from Engine.ResourceLoader import *
from . import MainMenu


class SplashScreen():
    """

    Used by game to make the SplashScreen
    """

    def __init__(self, gm):
        self.splash, self.splash_rect = ResourceLoader().load_image(
            'Splash1.png')
        self.sound = ResourceLoader().load_sound('Splash_Sound1.wav')
        self.button_one = ResourceLoader().make_button(
            (251, 251, 251), gm.screen_rect.width / 2 - 50,
            gm.screen_rect.height / 2 - 25, 100, 50, 0, "Click Me!", (10, 10,
                                                                      10))

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
                if self.button_one.pressed(pygame.mouse.get_pos()):
                    gm.current_screen = MainMenu.MainMenu(gm)
                    self.sound.play()

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
