import pygame
import data
import pinpongs_objects as po
import time

pygame.init()

window = pygame.display.set_mode((data.setting_win["WIDTH"], data.setting_win["HEIGHT"]))
pygame.display.set_caption(data.setting_win["NAME_GAME"])
def run():
    game = True
    clock = pygame.time.Clock()
    desk_player_left = po.Desk_player(data.setting_win["WIDTH"]//2-300, data.setting_win["HEIGHT"]//2, data.setting_desk_player["WIDTH"], data.setting_desk_player["HEIGHT"], data.setting_desk_player["SPEED"], data.desk_player_left_image)
    desk_player_right = po.Desk_player(data.setting_win["WIDTH"]-100, data.setting_win["HEIGHT"]//2, data.setting_desk_player["WIDTH"], data.setting_desk_player["HEIGHT"], data.setting_desk_player["SPEED"], data.desk_player_right_image)
    ball = po.Ball(data.setting_win["WIDTH"]//2 - data.setting_ball["RADIUS"], data.setting_win["HEIGHT"] // 2 - data.setting_ball["RADIUS"],data.setting_ball["RADIUS"])
    while game:
        window.blit(data.fon_image, (0,0))
        window.blit(desk_player_left.IMAGE, (desk_player_left.x, desk_player_left.y))
        window.blit(desk_player_right.IMAGE, (desk_player_right.x, desk_player_right.y))
        pygame.draw.circle(window, (255,255,255), (ball.X ,ball.Y), ball.RADIUS)
        desk_player_left.move()
        desk_player_right.move()
        ball.move(desk_player_left, desk_player_right)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    desk_player_left.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    desk_player_left.MOVE["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    desk_player_left.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    desk_player_left.MOVE["DOWN"] = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    desk_player_right.MOVE["UP"] = True
                if event.key == pygame.K_DOWN:
                    desk_player_right.MOVE["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    desk_player_right.MOVE["UP"] = False
                if event.key == pygame.K_DOWN:
                    desk_player_right.MOVE["DOWN"] = False
        
        clock.tick(90)
        pygame.display.flip()


run()