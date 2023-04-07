import pygame
import data
import pinpongs_objects as po

pygame.init()

window = pygame.display.set_mode((data.setting_win["WIDTH"], data.setting_win["HEIGHT"]))
pygame.display.set_caption(data.setting_win["NAME_GAME"])
def run():
    desk_player = pygame.Rect(data.setting_win["WIDTH"] // 2 - 300, data.setting_win["HEIGHT"], data.desk_player_image["WIDTH"], data.desk_player_image["HEIGHT"])
    game = True
    while game:
        window.fill(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    desk_player.MOVE["UP"] = True
        pygame.display.flip()


run()