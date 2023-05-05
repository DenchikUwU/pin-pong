import pygame
import data
import random
import json
import time

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
        
class Point():
    def __init__(self,name_left,name_right):
        self.NAME_LEFT = name_left
        self.NAME_RIGHT = name_right
        self.LEFT_POINT = 0
        self.RIGHT_POINT = 0
        self.FONT = pygame.font.Font(None,40)

    def blit_point(self, window):
        window.blit(self.FONT.render(f"{self.LEFT_POINT} : {self.RIGHT_POINT}", True, (200,255,255)), (data.setting_win["WIDTH"] // 2 - 50, 10))

class Ball():
    def __init__(self,x,y,radius,image=None, speed= 6):
        self.X = x
        self.Y = y
        self.RADIUS = radius
        self.RECT = pygame.Rect(x - radius, y - radius, (radius ** 2 + radius ** 2) ** 0.5, (radius ** 2 + radius ** 2) ** 0.5)
        self.IMAGE = image
        self.CONST = speed
        self.SPEED = random.choice([-speed, speed])
        self.ANGLE = 0
        self.POINT = Point("left", "right")
        self.a = {-1}
    
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
        if self.POINT.LEFT_POINT == 1 or self.POINT.RIGHT_POINT == 1:
            data.history[str(time.time())] ={self.POINT.NAME_LEFT: self.POINT.LEFT_POINT, self.POINT.NAME_RIGHT: self.POINT.RIGHT_POINT}
            with open("history.json", "w", encoding= "utf-8") as file:
                json.dump(data.history, file, indent= 4)

        self.SPEED = random.choice([-self.CONST, self.CONST])
        self.ANGLE = 0
        self.X , self.Y = data.restart["RESTART_BALL"]
        self.RECT.center = data.restart["RESTART_BALL"]
        desk_player_left.y = data.restart["RESTART_DESK_LEFT"][1]
        desk_player_right.y = data.restart["RESTART_DESK_RIGHT"][1]
        window.blit(data.fon_image, (0,0))
        window.blit(desk_player_left.IMAGE, (desk_player_left.x, desk_player_left.y))
        window.blit(desk_player_right.IMAGE, (desk_player_right.x, desk_player_right.y))
        pygame.draw.circle(window, (255,255,255), self.RECT.center, self.RADIUS)
        self.POINT.blit_point(window)
        pygame.display.flip()
        time.sleep(2)

    def move(self, desk_player_left, desk_player_right, window):
        if self.X - self.RADIUS <= 0:
            self.POINT.RIGHT_POINT += 1
            self.restart(desk_player_left, desk_player_right, window)
        elif self.X + self.RADIUS >= data.setting_win["WIDTH"]:
            self.POINT.LEFT_POINT += 1
            self.restart(desk_player_left, desk_player_right, window)
        
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
        self.RECT.y = self.Y
        self.X += self.SPEED
        self.RECT.x = self.X
        self.a.add((self.SPEED ** 2 + self.ANGLE ** 2) ** 0.5)

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
        x = 50
        for key_main in data.history.keys():
            window.blit(font.render(f"-", True, (0,0,0)), (225, y))
            for key, value in zip(data.history[key_main].keys(), data.history[key_main].values()):
                window.blit(font.render(f"{key} : {value}", True, (0,0,0)), (x,y))
                x += 300
            x = 50
            y += 50


