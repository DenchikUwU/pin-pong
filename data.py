import pygame
import json

history = dict()

with open("history.json", "r", encoding= "utf = 8") as file:
    history = json.load(file)

setting_win = {
    "WIDTH": 700,
    "HEIGHT": 400,
    "FPS": 60,
    "NAME_GAME": "Ping Pong"
}

setting_desk_player = {
    "WIDTH": 20,
    "HEIGHT": 150,
    "SPEED": 2.5
}

setting_ball = {
    "RADIUS": 15
}

desk_player_left_image = pygame.transform.scale(pygame.image.load("blue_desk.png"), (setting_desk_player["WIDTH"], setting_desk_player["HEIGHT"]))
desk_player_right_image = pygame.transform.scale(pygame.image.load("red_desk.png"), (setting_desk_player["WIDTH"], setting_desk_player["HEIGHT"]))
fon_image = pygame.image.load("fon.png")