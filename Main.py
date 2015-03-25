# coding=utf-8
"""
__Arthur Marble__
Main File for Hangman game. This is where all the magic starts.
"""
from Engine.GameManager import *


def main():
    """

    __Main Function__
    Call GameManger ( class) run_game_loop() function to start the main game
    loop. Imported from Engine directory/folder.
    """
    GameManager().run_game_loop()

if __name__ == '__main__':
    main()