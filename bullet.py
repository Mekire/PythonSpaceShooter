import pygame

black    = (   0,   0,   0)
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(black)
 
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 5
