# coding=utf-8
"""
__Arthur Marble__
Settings screen for the game.
"""
import pygame


def buttons_dict_maker(gm):
    """
    Make a dict of buttons for this GameView Class,
    Edit this for button placement.
    :param gm: Pass GameManger to get screen dimensions
    :return: buttons_dict
    """
    # TODO: Add code to update button position when screen resolution changes.
    buttons_dict = {}
    button_width = 200
    button_height = 50
    padding = 50
    x = gm.screen_rect.centerx - button_width / 2
    y = gm.screen_rect.centery - 150
    # print("x:", x, "y", y)  # DEBUGGING
    buttons_dict['fullscreen'] = gm.resource_loader.make_button(
        (251, 251, 255), x, y, button_width, button_height, 0,
                                                               'Fullscreen',
                                                            (10, 10, 10))
    y += (button_height + padding)
    buttons_dict['back'] = gm.resource_loader.make_button(
        (251, 251, 255), x, y, button_width, button_height, 0, 'Back',
                                                            (10, 10, 10))
    y += (button_height + padding)
    buttons_dict['quit'] = gm.resource_loader.make_button(
        (251, 251, 255), x, y, button_width, button_height, 0, 'Quit',
                                                            (10, 10, 10))
    return buttons_dict


def change_res(gm):
    """
    Change the resolution of the screen
    :param gm:
    :return:
    """
    if not gm.fullscreen:
        gm.fullscreen = True
        gm.screen = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
        gm.screen_rect = gm.screen.get_rect()
        #  print(gm.screen_rect)
        gm.current_screen = gm.resource_loader.load_class("main menu", gm)
    else:
        gm.fullscreen = False
        gm.screen = pygame.display.set_mode((640, 400))
        gm.screen_rect = gm.screen.get_rect()
        #  print(gm.screen_rect)
        gm.current_screen = gm.resource_loader.load_class("main menu", gm)


class Settings():
    """

    Settings screen for the game.
    """

    def __init__(self, gm):
        self.bg = pygame.Surface((gm.screen_rect.width, gm.screen_rect.height))
        self.bg_rect = self.bg.get_rect()
        self.bg_color = (180, 190, 180)
        self.bg.fill(self.bg_color)
        gm.screen.blit(self.bg, self.bg_rect)
        self.buttons = buttons_dict_maker(gm)
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
                if self.buttons['fullscreen'].pressed(
                        pygame.mouse.get_pos()):
                    self.b_sound2.play()
                    change_res(gm)
                elif self.buttons['back'].pressed(
                        pygame.mouse.get_pos()):
                    self.b_sound2.play()
                    gm.current_screen = gm.resource_loader.load_class("main menu", gm)
                elif self.buttons['quit'].pressed(
                        pygame.mouse.get_pos()):
                    self.b_sound2.play()
                    gm.playing = False
                else:
                    self.b_sound1.play()

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
        self.buttons['fullscreen'].draw_button(self.bg)
        self.buttons['back'].draw_button(self.bg)
        self.buttons['quit'].draw_button(self.bg)
        gm.screen.blit(self.bg, self.bg_rect)
        pygame.display.flip()
