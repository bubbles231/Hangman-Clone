# coding=utf-8
"""
__Arthur Marble__
This will be my SplashScreen for the game.
"""
import pygame


# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic
class SplashScreen(object):
    """

    Used by game to make the SplashScreen
    """

    def __init__(self, gm):
        self.splash, self.splash_rect = gm.resource_loader.load_image(
            'Splash1.png')
        self.b_sound1 = gm.resource_loader.load_sound('Splash_Sound1.wav')
        self.b_sound2 = gm.resource_loader.load_sound('MouseButtonDown.wav')
        self.button_one = gm.resource_loader.make_button(
            (251, 251, 251), gm.screen_rect.width / 2 - 50,
            gm.screen_rect.height / 2 - 25, 100, 50, 0, "Click Me", (10, 10, 10))
        if gm.fullscreen:
            pass  # It will never come to splash screen on fullscreen

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
                    gm.current_screen = gm.resource_loader.load_class(
                        "main menu", gm)
                    self.b_sound2.play()
                else:
                    self.b_sound1.play()

    # noinspection PyMethodMayBeStatic
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
