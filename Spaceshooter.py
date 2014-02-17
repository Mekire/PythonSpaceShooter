
import pygame
import random
from blocks import *
from player import *
from bullet import *

# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
red      = ( 255,   0,   0)
blue     = (   0,   0, 255)
              
 
# --- Create the window
 
# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# --- Sprite lists
 
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
 
# List of each bullet
bullet_list = pygame.sprite.Group()
 
# --- Create the sprites
 
for i in range(10):
    # This represents a block
    block = Block()
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
     
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a red player block
player = Player()
all_sprites_list.add(player)
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)
 
score = 0

level = 1
player.rect.y = 370
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

        
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.go_up()
                if event.key == pygame.K_DOWN:
                    player.go_down()
                     
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0: 
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
                if event.key == pygame.K_DOWN and player.change_y > 0: 
                    player.stop()
                if event.key == pygame.K_UP and player.change_y < 0:
                    player.stop()
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Fire a bullet if the user clicks the mouse button
                bullet = Bullet()
            # Set the bullet so it is where the player is
                bullet.rect.x = player.rect.x
                bullet.rect.y = player.rect.y
            # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)
 
    # --- Game logic
     
    # Call the update() method on all the sprites
    all_sprites_list.update()
     
    # Calculate mechanics for each bullet
    for bullet in bullet_list:
 
        # See if it hit a block
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
         
        # For each block hit, remove the bullet and add to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print( score )
             
        # Remove the bullet if it flies up off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

        if len(block_list) == 0:
            level += 1

            for i in range(level * 10):
                block = Block()

                block.rect.x = random.randrange(screen_width)
                block.rect.x = random.randrange(screen_height)

                block_list.add(block)
                all_sprites_list.add(block)

        
    # --- Draw a frame
 
    # Clear the screen
    screen.fill(white)
         
    # Draw all the spites
    all_sprites_list.draw(screen)

    text = font.render("Score: "+str(score), True, black)
    screen.blit(text, [10, 10])

    text = font.render("Level: "+str(level), True, black)
    screen.blit(text, [10, 40])
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
     
    # --- Limit to 20 frames per second
    clock.tick(20)
 
pygame.quit()
