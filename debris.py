#debris.py
import random
import pygame
import math

class debris(object):
    """the debris class"""
    def __init__(self, x, ang):
        self.image = pygame.image.load("img/logforqueendavid.png")
        self.scale = random.randrange(1, 2)
        self.image = pygame.transform.scale(self.image, (self.scale*self.image.get_rect().width, self.scale*self.image.get_rect().height))
        self.scale = random.randrange(1, 5)
        pygame.transform.scale(self.image, (self.scale*self.image.get_rect().width, self.scale*self.image.get_rect().height))
        self.rect = self.image.get_rect()
        self.type = "debris"
        #spawn debris at the top of the river
        self.rect.move_ip(x, 0)
        self.angle = ang
        self.xvel = 60
        self.yvel = 60 #should be fine now
        self.spinning = 0
        self.original = self.image
        self.frame = 0
        self.collided = False

    def update(self, FrameRate):
        """updates debris"""
        FrameRate = FrameRate/100
        self.collided = False
        self.frame += 1
        
        while self.angle > 2*math.pi or self.angle < -2*math.pi:
            if self.angle > 2*math.pi:
                self.angle -= 2*math.pi
            if self.angle < -2*math.pi:
                self.angle += 2*math.pi        
        
        return self.move(FrameRate)
    
    def displace(self, bubble_rect):
        if type == "Rock":
            return
        self.angle=-math.atan2(self.rect.centery-bubble_rect.centery, self.rect.centerx - bubble_rect.centerx)
        if self.yvel > -20:
            self.yvel -=20
        if self.angle > 0 and self.angle < math.pi/2:
            self.spinning = 1
        else:
            self.spinning = -1
        
        
    def move(self, FrameRate):
        """moves debris along its trajectory"""
        
        if self.yvel < 60:
            self.yvel += 5
        self.rect.move_ip(math.cos(self.angle)*self.xvel*FrameRate, -math.sin(self.angle)*self.yvel*FrameRate)

        #bounce off of the sides of the river
        if self.rect.left < 100:
            self.angle += math.pi/4
            self.spinning = -self.spinning
            self.rect.left = 100
        elif self.rect.right > 500:
            self.angle -= math.pi/4
            self.spinning = -self.spinning
            self.rect.right = 500
        
        return True

    def draw(self, screen):
        """draws the debris"""
        if self.frame % 30 == 0:
            self.image = pygame.transform.rotate(self.image, self.spinning*math.pi/4)
        screen.blit(self.image, self.rect)

class rock(debris):
    """unbreakable type debris"""
    def __init__(self, x, ang):
        debris.__init__(self, x, ang)
        #reset image, scale, and rect
        self.image = pygame.image.load("img/Rock.png")
        self.scale = random.randrange(1, 3)
        self.image = pygame.transform.scale(self.image, (self.scale*self.image.get_rect().width, self.scale*self.image.get_rect().height))
        self.rect = self.image.get_rect()
        self.type == "rock"
        self.rect.x = x
        self.xvel = 50
        self.yvel = 50
        self.ang = -math.pi/2
        self.spinning = False
        
        
    def update(self, FrameRate):
        """updates rock"""
        FrameRate = FrameRate/100
        self.collided = False
        self.frame += 1     
        
        return self.move(FrameRate)
    
    def move(self, FrameRate):
        """moves rock along its trajectory"""
        
        self.rect.move_ip(math.cos(self.angle)*self.xvel*FrameRate, -math.sin(self.angle)*self.yvel*FrameRate)

        #bounce off of the sides of the river
        if self.rect.left < 100:
            self.rect.left = 100
        elif self.rect.right > 500:
            self.rect.right = 500
