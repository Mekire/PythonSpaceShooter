import pygame

class Player(pygame.sprite.Sprite):
    """ This class represents the Player. """
    change_x = 0
    change_y = 0
    world_shift = 0
    def __init__(self):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self) 
 
        self.image = pygame.image.load("sprite.png").convert()
        
 
        self.rect = self.image.get_rect()
         
    def update(self):
        """ Update the player's position. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6

    def go_up(self):
        self.change_y = -6

    def go_down(self):
        self.change_y = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0 
        self.change_y = 0
