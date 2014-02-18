import pygame as pg
import bullet


#Dictionary of keys to unit vectors.
DIRECT_DICT = {pg.K_LEFT  : (-1, 0),
               pg.K_RIGHT : ( 1, 0),
               pg.K_UP    : ( 0,-1),
               pg.K_DOWN  : ( 0, 1)}


class Player(pg.sprite.Sprite):
    """This class represents the Player."""
    def __init__(self, image, position, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.speed = 5

    def shoot(self, *groups):
        """Create a bullet and add it to groups."""
        bullet.Bullet(self.rect.center, *groups)

    def update(self, keys, screen_rect):
        """Update the player's position and keep him on screen."""
        for key in DIRECT_DICT:
            if keys[key]:
                self.rect.x += DIRECT_DICT[key][0]*self.speed
                self.rect.y += DIRECT_DICT[key][1]*self.speed
        self.rect.clamp_ip(screen_rect) #Keep player on screen.
