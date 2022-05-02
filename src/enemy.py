import pygame
#import random

#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
      ''' 
      Initialize the enemy.
	    args: (str, int) Enemy name with unique ID, enemy location coordinantes, and image for enemy
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
      self.name = name + str(id(self))
      self.speed = 2

    def update(self, hero_y, hero_x):
      ''' 
      Updates the enemy location based on the hero location so enemy move towards hero.
	    args: (int) Hero location coordinantes.
	    return: None
      '''
      if self.rect.x > hero_x:
        self.rect.x -= 1
      if self.rect.y > hero_y:
        self.rect.y -= 1
      if self.rect.x < hero_x:
        self.rect.x += 1
      if self.rect.x < hero_x:
        self.rect.x += 1

      # self.rect.x = random.randrange(-1,2)
      # self.rect.y = random.randrange(-1,2)
