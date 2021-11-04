from os import supports_dir_fd
import pygame
#######################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('shot the ball') 

# FPS
clock = pygame.time.Clock()
#######################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/shot_the_ball/shot_the_ball_image/background.png')
stage = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/shot_the_ball/shot_the_ball_image/stage.png')
character = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/shot_the_ball/shot_the_ball_image/character.png')
weapon = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/shot_the_ball/shot_the_ball_image/weapon.png')
ball = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/shot_the_ball/shot_the_ball_image/ball.png')


# 캐릭터 설정
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height - stage.get_rect().size[1]

# 공 설정
class Ball():
    def __init__(self, n):
        self.ball_size = ball.get_rect().size
        self.ball_width = int(self.ball_size[0] / n)
        self.ball_height = int(self.ball_size[1] / n)
        self.ball_x_pos = screen_width - self.ball_width
        self.ball_y_pos = screen_height - self.ball_height - stage.get_rect().size[1]
    def seperate(self):
        pass

#무기 설정
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = character_x_pos
weapon_y_pos = character_y_pos





running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False 
            
        

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, 430))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ball, (Ball(1).ball_x_pos, Ball(1).ball_y_pos))



    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()