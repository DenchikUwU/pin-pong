import pygame
import data
import pinpongs_objects as po

pygame.init()

window = pygame.display.set_mode((data.setting_win["WIDTH"], data.setting_win["HEIGHT"]))
pygame.display.set_caption(data.setting_win["NAME_GAME"])
def run():
    game = True
    desk_player = po.Desk_player(data.setting_win["WIDTH"]//2-300, data.setting_win["HEIGHT"]//2, data.setting_desk_player["WIDTH"], data.setting_desk_player["HEIGHT"], data.setting_desk_player["SPEED"], data.desk_player_image)
    while game:
        window.blit(data.fon_image, (0,0))
        window.blit(desk_player.IMAGE, (desk_player.x, desk_player.y))
        desk_player.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    desk_player.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    desk_player.MOVE["DOWN"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    desk_player.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    desk_player.MOVE["DOWN"] = False
        pygame.display.flip()


run()