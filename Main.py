# coding=utf-8
"""

Main File for Hangman game. This is where all the magic
starts - Arthur Marble
"""
import os
import sys
import pygame

if not pygame.font:
    print('Warning, fonts disabled')  # TODO: Use fonts
if not pygame.mixer:
    print('Warning, sound disabled')  # TODO: Use sound


def load_image(name, color_key=None):
    """
    :param name: Name of the image
    :param color_key: A pygame option that I included from example online
    :return: Returns an image and the pygame.Rect() for that image
    """
    pathname = os.path.join('Resources', name)
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
    return image, image.rect()


def main():
    """
    Start with a splash screen.
    :return:
    """

    pygame.init()
    print("Make Splash Screen!...")
    pygame.quit()

if __name__ == '__main__':
    main()