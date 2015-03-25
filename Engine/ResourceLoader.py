# coding=utf-8
"""
__Arthur Marble__
ResourceLoader File
------------------------------------------------------
I will load any and all resources through the class
in this file.
I will also try to make all my main import statements here.
"""
import os
import re
import random
import pygame
from . import Buttons
from GameViews import MainMenu
from GameViews import Settings
from GameViews import SplashScreen
from GameViews import MainGame

if not pygame.font:
    print('Warning, fonts disabled')
if not pygame.mixer:
    print('Warning, sound disabled')


class ResourceLoader():
    """

    ResourceLoader Class
    I load all resources for my game here
    """

    def __init__(self):
        pass

    def load_class(self, string, gm):
        """
        Load GameView classes
        :param string:
        :param gm: GameManager
        :return: class
        """
        if string == "splash screen":
            return SplashScreen(gm)
        elif string == "main menu":
            return MainMenu(gm)
        elif string == "settings":
            return Settings(gm)
        elif string == "main game":
            return MainGame(gm)

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

    def get_words(self):
        """

        Get word list and return a random word
        :return:
        """
        file = open('Resources/Text/WordList.txt', 'r')
        text = file.read().lower()
        file.close()
        # replaces anything that is not a lowercase letter, a space, or an
        # apostrophe with a space:
        text = re.sub('[^a-z\ \']+', " ", text)
        words = list(text.split())
        # print("Words:\n", words)  # DEBUGGING
        word = random.choice(words)
        # print("The word is:", word)  # DEBUGGING
        return word

if __name__ == "__main__":
    ResourceLoader().get_words()