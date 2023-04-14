import pygame
import data
import random

class PinPong(pygame.Rect):
    def __init__(self,x,y,width,height,speed,image):
        super().__init__(x,y,width,height)
        self.IMAGE = image
        self.SPEED = speed
        self.MOVE = {"UP": False, "DOWN": False}

class Desk_player(PinPong):
    def __init__(self,x,y,width,height,speed,image):
        super().__init__(x,y,width,height,speed,image)
    
    def move(self):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < data.setting_win["HEIGHT"] - self.height:
            self.y += self.SPEED
        
class Ball():
    def __init__(self,x,y,radius,image=None, speed= 2):
        self.X = x
        self.Y = y
        self.RADIUS = radius
        self.IMAGE = image
        self.CONST = speed
        self.SPEED = random.choice([-speed, speed])
        self.ANGLE = 0
    
    def make_angle(self, ang):
        if self.SPEED < 0:
            self.SPEED = -self.CONST
        elif self.SPEED > 0:
            self.SPEED = self.CONST
        self.ANGLE = ang * uniform(abs(self.SPEED //2), abs(self.SPEED))
        coff = abs(self.SPEED) / abs((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)
        self.ANGLE *= coff 
        self.SPEED *= coff

    def move(self, desk_player_left, desk_player_right):
        if self.Y - self.RADIUS <= 0 or self.Y + self.RADIUS >= data.setting_win["HEIGHT"]:
            self.ANGLE *= -1
        elif desk_player_left.collidepoint(self.X - self.RADIUS, self.Y):
            self.SPEED *= -1
            if desk_player_left.MOVE["UP"]:
                #self.ANGLE = -uniform(abs(self.SPEED //2), abs(self.SPEED))
                self.make_angle(-1)
            elif desk_player_left.MOVE["DOWN"]:
                #self.ANGLE = uniform(abs(self.SPEED //2), abs(self.SPEED))
                self.make_angle(1)
        elif desk_player_right.collidepoint(self.X - self.RADIUS, self.Y):
            self.SPEED *= -1
            if desk_player_right.MOVE["UP"]:
                #self.ANGLE = -uniform(abs(self.SPEED //2), abs(self.SPEED))
                self.make_angle(-1)
            elif desk_player_right.MOVE["DOWN"]:
                #self.ANGLE = uniform(abs(self.SPEED //2), abs(self.SPEED))
                self.make_angle(1)

        self.Y += self.ANGLE
        self.X += self.SPEED
