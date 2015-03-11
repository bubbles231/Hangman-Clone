# coding=utf-8
"""
Original module by Simon H. Larsen: http://lagusan.com/button-drawer-python-2-6/
Modified by Arthur Marble
"""
import pygame
from pygame.locals import *


class Button:
    """
    'The idea was to create a dynamic module which would create a button from
    several parameters. But it should also be kept on a simple and logical
    way. If you want a more advanced button drawer, then I recommend zModule
    for Python.' -- Simon H. Larsen
    """

    def __init__(self, gm_screen, color, x, y, length, height, width, text,
                 text_color):
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.height = height
        self.width = width
        self.text = text
        self.text_color = text_color
        self.rect = pygame.Rect(self.x, self.y, self.length, self.height)

    def write_text(self, surface):
        font_size = int(self.length//len(self.text))
        my_font = pygame.font.SysFont("Calibri", font_size)
        my_text = my_font.render(self.text, 1, self.text_color)
        surface.blit(my_text, ((self.x+self.length/2) - my_text.get_width()/2,
                               (self.y+self.height/2) - my_text.get_height()/2))
        return surface

    def draw_button(self, surface):
        for i in range(1,10):
            s = pygame.Surface((self.length+(i*2),self.height+(i*2)))
            s.fill(self.color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, self.color, (self.x-i,self.y-i,self.length+i,
                                        self.height+i), self.width)
            surface.blit(s, (self.x-i,self.y-i))
        pygame.draw.rect(surface, self.color, (self.x,self.y,self.length,
                                          self.height), 0)
        pygame.draw.rect(surface, (190,190,190), (self.x,self.y,self.length,
                                                  self.height), 1)
        self.write_text(surface)


    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False
