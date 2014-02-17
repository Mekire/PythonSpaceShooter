import pygame
import random

black    = (   0,   0,   0)
class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.image.load("rock.png").convert()
        self.image.set_colorkey(black)

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(700-20)

    def update(self):
        self.rect.y += 1

        if self.rect.y > 410:
            self.reset_pos()
