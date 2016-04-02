import sys
import pygame
from pygame.locals import *
from random import randrange


class Weight(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.count = 0
        self.image = weight_image
        self.rect  = self.image.get_rect()
        self.reset()

    def reset(self):
        """
        move the weight to the top of scree
        :return: None
        """
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(screen_size[0])

    def update(self):
        """
        Update weight, show the next frame
        :return:
        """
        self.count += 1
        if (self.count / 5 == 1):
            self.count = 0
            self.rect.top += 1
        if self.rect.top > screen_size[1]:
            self.reset()

pygame.init()
screen_size = 800, 600
pygame.display.set_mode(screen_size, 0, 32)
pygame.mouse.set_visible(False)

weight_image = pygame.image.load("weight.png")
weight_image = weight_image.convert()

sprites = pygame.sprite.RenderUpdates()
sprites.add(Weight())

screen = pygame.display.get_surface()
background_color = (255, 255, 255)
screen.fill(background_color)
pygame.display.flip()


def clear_callback(surf, rect):
    surf.fill(background_color, rect)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()

    sprites.clear(screen, clear_callback)
    sprites.update()
    updates = sprites.draw(screen)
    pygame.display.update(updates)



