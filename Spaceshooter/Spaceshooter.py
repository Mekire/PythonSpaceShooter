import sys
import random
import pygame as pg
import blocks
import player


# Define some colors
BLACK    = (  0,   0,   0)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
BLUE     = (  0,   0, 255)


# Set the height and width of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400


class Control(object):
    """Class that manages primary conrol flow for the whole program."""
    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 20.0
        self.keys = pg.key.get_pressed()
        self.done = False
        self.font = pg.font.Font(None, 36)
        self.setup_sprites()
        self.score = 0
        self.level = 1

    def setup_sprites(self):
        """Create all our sprite groups."""
        self.all_sprites = pg.sprite.Group()
        self.blocks = pg.sprite.Group()
        self.bullets = pg.sprite.Group()
        self.player = player.Player(PLAYER_IMAGE, (0,370), self.all_sprites)
        self.make_blocks(10)

    def make_blocks(self, amount):
        """Create block instances, placing them in the appropriate groups."""
        for i in range(amount):
            x = random.randrange(SCREEN_WIDTH-ROCK_IMAGE.get_width())
            y = random.randrange(SCREEN_HEIGHT)
            blocks.Block(ROCK_IMAGE, (x,y), self.blocks, self.all_sprites)

    def event_loop(self):
        """Event loop for program; there can be only one."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type in (pg.KEYDOWN, pg.KEYUP):
                self.keys = pg.key.get_pressed()
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.player.shoot(self.bullets, self.all_sprites)

    def update(self):
        """Update all sprites and check collisions."""
        self.all_sprites.update(self.keys, self.screen_rect)
        hits = pg.sprite.groupcollide(self.bullets, self.blocks, True, True)
        self.score += sum(len(hits[hit]) for hit in hits)
        if not self.blocks:
            self.level += 1
            self.make_blocks(self.level*10)

    def draw(self):
        """Draw all items to the screen."""
        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        text = self.font.render("Score: {}".format(self.score), True, BLACK)
        self.screen.blit(text, (10,10))
        text = self.font.render("Level: {}".format(self.level), True, BLACK)
        self.screen.blit(text, (10,40))

    def main_loop(self):
        """
        This is the main program loop; as with the event loop, there can
        be only one.
        """
        while not self.done:
            self.event_loop()
            self.update()
            self.draw()
            pg.display.update()
            self.clock.tick(self.fps)


def main():
    """
    Initialize pygame and prepare the display.  Then create an instance of
    Control and call the main_loop.  Graphic loading is done here; in a more
    complex program it would be done in a seperate module.
    """
    global PLAYER_IMAGE, ROCK_IMAGE
    pg.init()
    pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    PLAYER_IMAGE = pg.image.load("sprite.png").convert()
    PLAYER_IMAGE.set_colorkey(WHITE)
    ROCK_IMAGE = pg.image.load("rock.png").convert()
    ROCK_IMAGE.set_colorkey(WHITE)
    app = Control()
    app.main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
