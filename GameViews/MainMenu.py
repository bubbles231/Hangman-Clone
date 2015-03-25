# coding=utf-8
"""
__Arthur Marble__
This will be my MainMenu for the game.
"""
from Engine.ResourceLoader import *


def buttons_dict_maker(gm):
    """
    Make a dict of buttons for this GameView Class,
    Edit this for button placement.
    :param gm: Pass GameManger to get screen dimensions
    :return: buttons_dict
    """
    # TODO: Don't hardcode button placement.
    buttons_dict = {}
    button_width = 200
    button_height = 100
    x, y = (gm.screen_width // 2 - button_width), (gm.screen_height // 2 -
                                                   button_height)
    buttons_dict['start 1 player'] = ResourceLoader().make_button(
        (251, 251, 255), x, y, button_width, button_height, 0, 'Start 1 '
                                                               'Player',
                                                            (10, 10, 10))
    buttons_dict['settings'] = ResourceLoader().make_button(
        (251, 251, 255), 100, 150, 200, 50, 0, 'Settings', (10, 10, 10))
    buttons_dict['quit'] = ResourceLoader().make_button(
        (251, 251, 255), 200, 250, 100, 50, 0, 'Quit!', (10, 10, 10))

    return buttons_dict


class MainMenu():
    """

    Used by game to make the MainMenu.
    """

    def __init__(self, gm):
        self.bg = pygame.Surface((gm.screen_height, gm.screen_width))
        self.bg_rect = self.bg.get_rect()
        self.bg_color = ((100, 140, 50))
        self.bg.fill(self.bg_color)
        gm.screen.blit(self.bg, self.bg_rect)
        self.buttons = buttons_dict_maker(gm)

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
                if self.buttons['start 1 player'].pressed(
                        pygame.mouse.get_pos()):
                    print("Start has been pressed!")     # TODO: MainGame GV
                elif self.buttons['settings'].pressed(
                        pygame.mouse.get_pos()):
                    print("Settings has been pressed!")  # TODO: Settings GV
                elif self.buttons['quit'].pressed(
                        pygame.mouse.get_pos()):
                    # print("Quit has been pressed!")    # DEBUGGING
                    gm.playing = False

    def recalculate(self, gm):
        """

        Recalculate logic
        :param gm: GameManager class
        :return: None
        """
        pass

    def render(self, gm):
        """

        Render the screen.
        :param gm: GameManager class
        :return: None
        """
        self.buttons['start 1 player'].draw_button(self.bg)
        self.buttons['settings'].draw_button(self.bg)
        self.buttons['quit'].draw_button(self.bg)
        gm.screen.blit(self.bg, self.bg_rect)
        pygame.display.flip()
