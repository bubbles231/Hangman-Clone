# coding=utf-8
"""

Main File for Hangman game. This is where all the magic
starts - Arthur Marble
"""
from Engine.ResourceLoader import *


def main():
    """
    Start with a splash screen.
    :return:
    """

    pygame.init()
    splash, splash_rect = ResourceLoader().load_image('Splash1.png')
    sound = ResourceLoader().load_sound('Splash_Sound1.wav')
    screen = pygame.display.set_mode((640, 400))
    pygame.display.set_caption("Hangman Clone!")
    playing = True
    while playing:
        # Main Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sound.play()
        screen.blit(splash, splash_rect)
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # TODO: MAKE FPS ADJUSTABLE
    pygame.quit()


if __name__ == '__main__':
    main()