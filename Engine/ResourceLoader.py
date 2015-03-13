# coding=utf-8
"""

ResourceLoader File
------------------------------------------------------
I will load any and all resources through the class
in this file.
I will also try to make all my main import statements here.
"""
import os
import pygame
from . import Buttons
pygame.mixer.init(8000)  # All sound effects will have this sample rate

if not pygame.font:
    print('Warning, fonts disabled')  # TODO: Use fonts
if not pygame.mixer:
    print('Warning, sound disabled')


class ResourceLoader():
    """

    ResourceLoader Class
    I load all resources for my game here
    """

    def __init__(self):
        pass

    def load_image(self, name, color_key=None):
        """

        :param name: Name of the image file
        :param color_key: A pygame option that I included from example online
        :return: Returns an image and the pygame.Rect() for that image
        """
        pathname = os.path.join('Resources/Images/', name)
        try:
            image = pygame.image.load(pathname)
        except pygame.error:
            print('Cannot load image:', name)
            print("Quitting!\n")
            raise SystemExit
        if color_key is not None:
            if color_key is -1:
                color_key = image.get_at((0, 0))
            image.set_colorkey(color_key, pygame.RLEACCEL)
        return image, image.get_rect()

    def load_sound(self, name):
        """

        :param name: Name of the sound file
        :return: Pygame sound file
        """
        class NoneSound:
            """

            Empty class if system can't use pygame.mixer
            """

            def __init__(self):
                pass

            def play(self):
                """

                Function made for compatibility
                """
                pass

        if not pygame.mixer:
            return NoneSound()
        fullname = os.path.join('Resources/Sounds/', name)
        try:
            sound = pygame.mixer.Sound(fullname)
        except pygame.error:
            print('Cannot load sound:', name)
            print("Quitting!\n")
            raise SystemExit
        return sound

    def make_button(self, color=(107, 142, 35), x=0, y=0, length=200,
                    height = 100, width=1, text="Example", text_color=(255,
                                                                       255,
                                                                       255)):
        """

        Makes me a button.
        :type color: tuple
        :type x: int or float
        :type y: int or float
        :type length: int
        :type height: int
        :type width: int
        :type text: str
        :type text_color: tuple
        :return: Button.Button()
        """
        button = Buttons.Button(color, x, y, length, height, width,
                                text, text_color)
        return button