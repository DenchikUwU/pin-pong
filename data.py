import pygame

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

desk_player_left_image = pygame.image.load("blue_desk.png")
desk_player_right_image = pygame.image.load("red_desk.png")
fon_image = pygame.image.load("fon.png")