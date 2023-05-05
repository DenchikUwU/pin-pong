import pygame
import json

history = dict()

with open("history.json", "r", encoding= "utf-8") as file:
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

restart = {
    "RESTART_BALL": (setting_win["WIDTH"] // 2 - setting_ball["RADIUS"], setting_win["HEIGHT"] // 2 - setting_ball["RADIUS"]),
    "RESTART_DESK_LEFT": (15, setting_win["HEIGHT"] // 2 - setting_desk_player["HEIGHT"] // 2),
    "RESTART_DESK_RIGHT": (setting_win["WIDTH"] - setting_desk_player["WIDTH"] - 15, setting_win["HEIGHT"] // 2 - setting_desk_player["HEIGHT"] // 2)
}

desk_player_left_image = pygame.transform.scale(pygame.image.load("blue_desk.png"), (setting_desk_player["WIDTH"], setting_desk_player["HEIGHT"]))
desk_player_right_image = pygame.transform.scale(pygame.image.load("red_desk.png"), (setting_desk_player["WIDTH"], setting_desk_player["HEIGHT"]))
fon_image = pygame.image.load("fon.png")