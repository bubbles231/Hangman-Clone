# coding=utf-8
"""
__Arthur Marble__
This will be the main game class.
"""
import pygame


class MainGame():
    """

    The main game class.
    :return:
    """

    def __init__(self, gm):
        self.word = None
        self.bg = pygame.Surface((gm.screen_rect.width, gm.screen_rect.height))
        self.bg_rect = self.bg.get_rect()
        self.bg_color = (10, 35, 140)
        self.bg.fill(self.bg_color)
        gm.screen.blit(self.bg, self.bg_rect)
        self.b_sound1 = gm.resource_loader.load_sound('Splash_Sound1.wav')
        self.b_sound2 = gm.resource_loader.load_sound('MouseButtonDown.wav')

    def get_input(self, gm):
        """

        :param gm:
        :return:
        """
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and
                    event.key == pygame.K_ESCAPE):
                gm.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.b_sound1.play()
                print("Mousebutton down!")
                self.word = gm.resource_loader.get_words()
                print("self.word:", self.word)

    def recalculate(self, gm):
        """

        :param gm:
        :return:
        """
        pass

    def render(self, gm):
        """

        :param gm:
        :return:
        """
        pygame.display.update()