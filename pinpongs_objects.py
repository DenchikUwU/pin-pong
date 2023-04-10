import pygame
import data

class PinPong(pygame.Rect):
    def __init__(self,x,y,width,height,speed,image):
        super().__init__(x,y,width,height)
        self.IMAGE = image
        self.SPEED = speed

class Desk_player(PinPong):
    def __init__(self,x,y,width,height,speed,image):
        super().__init__(x,y,width,height,speed,image)
        self.MOVE = {"UP": False, "DOWN": False}
    
    def move(self):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < data.setting_win["HEIGHT"] - self.height:
            self.y += self.SPEED

class Desk_bot(PinPong):
    def __init__(self,x,y,width,height,speed):
        pass
        
