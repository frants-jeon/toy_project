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
ball = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/shot_the_ball/shot_the_ball_image/ball_test.png')


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
        if n < 4:
            Ball(n + 1)
    
    def seperate(self):
        pass

    def move(self):
        
        pass


#무기 설정
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = character_x_pos
weapon_y_pos = character_y_pos + character_height


# 좌표 설정
to_left = 0
to_right = 0
to_up = 0

#스피드 설정
character_speed = 10
weapon_speed = 10
ball_speed = 5


running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False 

        if event.type == pygame.KEYDOWN:
            # 캐릭터 움직임 설정
            if event.key == pygame.K_LEFT:
                to_left += character_speed
            elif event.key == pygame.K_RIGHT:
                to_right += character_speed
            elif event.key == pygame.K_UP:
                character_speed += 1
            elif event.key == pygame.K_DOWN:
                character_speed -= 1
            #무기 움직임 설정
            if event.key == pygame.K_LSHIFT:
                to_up += weapon_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = 0
            elif event.key == pygame.K_RIGHT:
                to_right = 0
            
            
        

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_right
    character_x_pos -= to_left

    # 무기 위치 정의
    if weapon_y_pos >= screen_height - 50: # stage height
        weapon_x_pos += to_right
        weapon_x_pos -= to_left
    
    if weapon_y_pos >= 0 - weapon_height:
        weapon_y_pos -= to_up
    else:
        to_up = 0
        weapon_x_pos = character_x_pos
        weapon_y_pos = character_y_pos + character_height

    # 공 위치 정의
    

    # 4. 충돌 처리

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    screen.blit(stage, (0, 430))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ball, (Ball(1).ball_x_pos, Ball(1).ball_y_pos))
    pygame.transform.scale2x(ball, ball) 



    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()