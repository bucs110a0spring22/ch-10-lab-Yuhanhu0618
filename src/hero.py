import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
      ''' 
      Initialize the hero.
	    args: (str, int) Hero name, hero location coordinante, and image for the hero.
	    return: None
      '''
      #initialize all the Sprite functionality
      pygame.sprite.Sprite.__init__(self)

      #The following two attributes must be called image and rect
      #pygame assumes you have intitialized these values
      #and uses them to update the screen

      #create surface object image
      self.image = pygame.image.load(img_file).convert_alpha()
      #get the rectangle for positioning
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      #set other attributes
      self.name = name
      self.speed = 3
      self.health = 3

    #methods to make moving our hero easier
    def move_up(self):
      ''' 
      Make the hero move up.
	    args: None
	    return: None
      '''
      self.rect.y -= self.speed
    def move_down(self):
      ''' 
      Make the hero move down.
	    args: None
	    return: None
      '''
      self.rect.y += self.speed
    def move_left(self):
      ''' 
      Make the hero move left
	    args: None
	    return: None
      '''
      self.rect.x -= self.speed
    def move_right(self):
      ''' 
      Make the hero move right
	    args: None
	    return: None
      '''
      self.rect.x += self.speed

    def fight(self, opponent):
      ''' 
      Make the hero fight if collide with an enemy
	    args: (pygame sprite object) The enemy object
	    return: (boolean) The result of the attack
      '''
      if(random.randrange(3)):
        self.health -= 1
        print("attack failed. Remaining Health: ", self.health)
        return False
      else:
        print("successful attack")
        return True
