import pygame
import data
import random
import json

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
    def __init__(self,x,y,radius,image=None, speed= 6):
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
        self.ANGLE = ang * random.uniform(abs(self.SPEED //2), abs(self.SPEED))
        coff = abs(self.SPEED) / abs((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)
        self.ANGLE *= coff 
        self.SPEED *= coff

    def restart(self, desk_player_left, desk_player_right, window):
        if self.POINT.LEFT_POINT ==11 or self.POINT.RIGHT_POINT:
            history[str(time.time())] ={self.POINT.NAME_LEFT: self.POINT.LEFT_POINT, self.POINT.NAME_RIGHT: self.POINT.RIGHT_POINT}
            with open("history.json", "w", encoding= "utf-8") as file:
                json.dump(history, file, indent= 4)

        self.SPEED = random.choice([-self.CONST, self.CONST])

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

class Menu():
    def __init__(self,width,height,count):
        #super().__init__(x,y,width,height)
        self.BUTTONS = list()
        self.COUNT = count
        self.width = width
        self.height = height
        self.FONT = pygame.font.SysFont("Comic Sans MS", 40)
        for button in range(count):
            self.BUTTONS.append(pygame.Rect(data.setting_win["WIDTH"]// 2 - width//2,data.setting_win["HEIGHT"]//2 - count * ((height+15) // 2) + (height + 15) * button, width,height))
    
    def draw_menu(self, window):
        window.fill((255,255,200))
        for button in self.BUTTONS:
            pygame.draw.rect(window, (100,130,200), button)
        window.blit(self.FONT.render("Start", True, (0,0,0)), (data.setting_win["WIDTH"]// 2 - self.width//2 + 50, data.setting_win["HEIGHT"]//2 - self.COUNT * ((self.height+15) // 2) + (self.height + 15) * 0 - 7))
        window.blit(self.FONT.render("Mode", True, (0,0,0)), (data.setting_win["WIDTH"]// 2 - self.width//2 + 50, data.setting_win["HEIGHT"]//2 - self.COUNT * ((self.height+15) // 2) + (self.height + 15) * 1 - 7))
        window.blit(self.FONT.render("History", True, (0,0,0)), (data.setting_win["WIDTH"]// 2 - self.width//2 + 30, data.setting_win["HEIGHT"]//2 - self.COUNT * ((self.height+15) // 2) + (self.height + 15) * 2 - 7))
        window.blit(self.FONT.render("Exit", True, (0,0,0)), (data.setting_win["WIDTH"]// 2 - self.width//2 + 58, data.setting_win["HEIGHT"]//2 - self.COUNT * ((self.height+15) // 2) + (self.height + 15) * 3 - 7))
    def click(self, cord):
        if self.BUTTONS[0].collidepoint(cord):
            return 1
        if self.BUTTONS[2].collidepoint(cord):
            return 3
        return 0

    def show_history(self, window):
        window.fill((255,255,200))
        font = pygame.font.Font(None, 25)
        y = 10
        for key in history.keys():
            window.blit(font.render(f"{key}    -    {history[key]}", True, (0,0,0)), (10, y))
            y += 50


