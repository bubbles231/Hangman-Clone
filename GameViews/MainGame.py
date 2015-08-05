
# coding=utf-8
"""
__Arthur Marble__
This will be the main game class.
"""
import pygame


class MainGame(object):
    """

    The main game class.
    :return:
    """

    def __init__(self, gm):
        self.word = {}
        tmp_word = gm.resource_loader.get_words()
        for i in range(0, len(tmp_word)):
            self.word[i] = tmp_word[i]
        self.guess_word = {}
        for i in range(0, len(self.word)):
            self.guess_word[i] = "_"
        print("Welcome to Hangman!")
        print(self.print_my_word(self.guess_word))
        self.hangman_cnt = 7
        self.key_guess = ""
        self.already_guess = []
        self.bg = pygame.Surface((gm.screen_rect.width, gm.screen_rect.height))
        self.bg_rect = self.bg.get_rect()
        self.bg_color = (200, 200, 200)
        self.bg.fill(self.bg_color)
        gm.screen.blit(self.bg, self.bg_rect)
        self.b_sound1 = gm.resource_loader.load_sound('Splash_Sound1.wav')
        self.b_sound2 = gm.resource_loader.load_sound('MouseButtonDown.wav')

        # Debug
        self.gw_button = gm.resource_loader.make_button(
            (251, 251, 251), 0, gm.screen_rect.height - 50, 100, 50, 0,
            self.print_my_word(self.guess_word), (10, 10, 10))

    def get_input(self, gm):
        """

        :param gm:
        :return:
        """
        for event in pygame.event.get():
            if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and
                    event.key == pygame.K_ESCAPE):
                gm.playing = False
            key_guess = ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    key_guess = 'a'
                elif event.key == pygame.K_b:
                    key_guess = 'b'
                elif event.key == pygame.K_c:
                    key_guess = 'c'
                elif event.key == pygame.K_d:
                    key_guess = 'd'
                elif event.key == pygame.K_e:
                    key_guess = 'e'
                elif event.key == pygame.K_f:
                    key_guess = 'f'
                elif event.key == pygame.K_g:
                    key_guess = 'g'
                elif event.key == pygame.K_h:
                    key_guess = 'h'
                elif event.key == pygame.K_i:
                    key_guess = 'i'
                elif event.key == pygame.K_j:
                    key_guess = 'j'
                elif event.key == pygame.K_k:
                    key_guess = 'k'
                elif event.key == pygame.K_m:
                    key_guess = 'm'
                elif event.key == pygame.K_n:
                    key_guess = 'n'
                elif event.key == pygame.K_l:
                    key_guess = 'l'
                elif event.key == pygame.K_o:
                    key_guess = 'o'
                elif event.key == pygame.K_p:
                    key_guess = 'p'
                elif event.key == pygame.K_q:
                    key_guess = 'q'
                elif event.key == pygame.K_r:
                    key_guess = 'r'
                elif event.key == pygame.K_s:
                    key_guess = 's'
                elif event.key == pygame.K_t:
                    key_guess = 't'
                elif event.key == pygame.K_u:
                    key_guess = 'u'
                elif event.key == pygame.K_v:
                    key_guess = 'v'
                elif event.key == pygame.K_w:
                    key_guess = 'w'
                elif event.key == pygame.K_x:
                    key_guess = 'x'
                elif event.key == pygame.K_y:
                    key_guess = 'y'
                elif event.key == pygame.K_z:
                    key_guess = 'z'
                self.key_guess = key_guess

    def recalculate(self, gm):
        """

        :param gm:
        :return:
        """
        if self.hangman_cnt == 0:
            print("You Lost! :(")
            print("The word was:")
            print(self.print_my_word(self.word))
            gm.current_screen = gm.resource_loader.load_class("main menu", gm)

        if self.key_guess != "":
            self.check_guess(self.key_guess, gm)
        self.key_guess = ""

    def render(self, gm):
        """

        :param gm:
        :return:
        """
        self.gw_button.draw_button(gm.screen)
        pygame.display.update()

    def check_guess(self, guess, gm):
        for i in self.already_guess:
            if guess == i:
                print("You have already guessed this letter!")
                return
        correct_guess = False
        for i in self.word:
            if guess == self.word[i]:
                self.guess_word[i] = self.word[i]
                correct_guess = True

        if correct_guess:
            print("Good Guess, you found a letter!")
            print(self.print_my_word(self.guess_word))
            self.already_guess.append(guess)
            self.gw_button.text = self.print_my_word(self.guess_word)
            if self.guess_word == self.word:
                print("You Win!")
                gm.current_screen = gm.resource_loader.load_class(
                    "main menu", gm)
        else:
            print("That letter isn't in the word, try again...")
            print("What you have guessed so far:")
            self.already_guess.append(guess)
            print(self.print_my_word(self.guess_word))
            self.hangman_cnt -= 1

    @staticmethod
    def print_my_word(word):
        tmp = ""
        for i in word:
            tmp += word[i]
        return tmp
