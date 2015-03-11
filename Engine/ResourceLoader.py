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