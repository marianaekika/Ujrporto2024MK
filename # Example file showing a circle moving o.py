# Example file showing a circle moving on screen
import pygame
import sys
import random
import math
import os
import getopt

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))

#load image and returne image object
def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

#game caractheres
#ball programation exemple
class Ball(pygame.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('ball.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

#ball bat exemple
class Bat(pygame.sprite.Sprite):
    """Movable tennis 'bat' with which one hits the ball
    Returns: bat object
    Functions: reinit, update, moveup, movedown
    Attributes: which, speed"""

    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("bat.png")
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.side = side
        self.speed = 10
        self.state = "still"
        self.reinit()

    def reinit(self):
        self.state = "still"
        self.movepos = [0,0]
        if self.side == "left":
            self.rect.midleft = self.area.midleft
        elif self.side == "right":
            self.rect.midright = self.area.midright

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        pygame.event.pump()

    def moveup(self):
        self.movepos[1] = self.movepos[1] - (self.speed)
        self.state = "moveup"

    def movedown(self):
        self.movepos[1] = self.movepos[1] + (self.speed)
        self.state = "movedown"
for event in pygame.event.get():
    if event.type == QUIT:
        return
    elif event.type == KEYDOWN:
        if event.key == K_UP:
            player.moveup()
        if event.key == K_DOWN:
            player.movedown()
    elif event.type == KEYUP:
        if event.key == K_UP or event.key == K_DOWN:
            player.movepos = [0,0]
            player.state = "still"

#let the ball hit sides
if not self.area.contains(newpos):
      tl = not self.area.collidepoint(newpos.topleft)
      tr = not self.area.collidepoint(newpos.topright)
      bl = not self.area.collidepoint(newpos.bottomleft)
      br = not self.area.collidepoint(newpos.bottomright)
      if tr and tl or (br and bl):
              angle = -angle
      if tl and bl:
              self.offcourt(player=2)
      if tr and br:
              self.offcourt(player=1)

self.vector = (angle,z)

#let the ball hit bats
else:
    # Deflate the rectangles so you can't catch a ball behind the bat
    player1.rect.inflate(-3, -3)
    player2.rect.inflate(-3, -3)

    # Do ball and bat collide?
    # Note I put in an odd rule that sets self.hit to 1 when they collide, and unsets it in the next
    # iteration. this is to stop odd ball behaviour where it finds a collision *inside* the
    # bat, the ball reverses, and is still inside the bat, so bounces around inside.
    # This way, the ball can always escape and bounce away cleanly
    if self.rect.colliderect(player1.rect) == 1 and not self.hit:
        angle = math.pi - angle
        self.hit = not self.hit
    elif self.rect.colliderect(player2.rect) == 1 and not self.hit:
        angle = math.pi - angle
        self.hit = not self.hit
    elif self.hit:
        self.hit = not self.hit
self.vector = (angle,z)

