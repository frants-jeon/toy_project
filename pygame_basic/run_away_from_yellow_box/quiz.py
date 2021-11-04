import pygame
import random
import os


# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('run away from yellow box') 

# FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 설정
background = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/run_away_from_yellow_box/background.png')

# 게임 폰트
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 30

# 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

# 피한 개수
avoid_cnt = 0

# yellow box 생성
class YellowBox():
    global screen_width
    global screen_height
    global avoid_cnt

    def __init__(self, yellow_box_x_pos : int = 0 , yellow_box_y_pos : int = 0 ):
        self.yellow_box = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/run_away_from_yellow_box/enemy.png')
        yellow_box_size = self.yellow_box.get_rect().size
        self.yellow_box_width = yellow_box_size[0] 
        self.yellow_box_height = yellow_box_size[1]
        self.yellow_box_x_pos = yellow_box_x_pos
        self.yellow_box_y_pos = yellow_box_y_pos
        # self.yellow_box_rect = self.yellow_box.get_rect()
        # self.yellow_box_rect.left = self.yellow_box_x_pos
        # self.yellow_box_rect.top = self.yellow_box_y_pos

    def reset(self):
        global avoid_cnt
        if self.yellow_box_y_pos <= screen_height - self.yellow_box_height:
            self.yellow_box_y_pos += random.randrange(1, 20)
        if self.yellow_box_y_pos >= screen_height - self.yellow_box_height:
            self.yellow_box_y_pos = 0
            self.yellow_box_x_pos = random.randrange(0, screen_width - self.yellow_box_width)
            avoid_cnt += 1
    def yrect(self):
        self.yellow_box_rect = self.yellow_box.get_rect()
        self.yellow_box_rect.left = self.yellow_box_x_pos
        self.yellow_box_rect.top = self.yellow_box_y_pos


yb1 = YellowBox(100)
yb2 = YellowBox(200,400)
yb3 = YellowBox(200,300)
yb4 = YellowBox(300,200)
yb5 = YellowBox(400,100)


# 캐릭터 생성
character = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/run_away_from_yellow_box/character.png')
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# 캐릭터 속도
character_speed = 0.5

# 좌표 생성
to_left = 0
to_right = 0
to_up = 0
to_down = 0


running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:  
        #     running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left += character_speed
            elif event.key == pygame.K_RIGHT:
                to_right += character_speed
            elif event.key == pygame.K_UP:
                if character_speed < 3:
                    character_speed += 0.2
            elif event.key == pygame.K_DOWN:
                if character_speed > 0.4:
                    character_speed -= 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = 0
            elif event.key == pygame.K_RIGHT:
                to_right = 0
            
        

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_right * dt
    character_x_pos -= to_left * dt
    # character_y_pos += to_up
    # character_y_pos -= to_down
    yb1.reset()
    yb2.reset()
    yb3.reset()
    yb4.reset()
    yb5.reset()


    if character_x_pos >= screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_x_pos <= 0:
        character_x_pos = 0
    # if character_y_pos >= screen_height - character_height:
    #     character_y_pos = screen_height - character_height
    # elif character_y_pos <= 0:
    #     character_y_pos = 0
    

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    yb1.yellow_box_rect = yb1.yellow_box.get_rect()
    yb1.yellow_box_rect.left = yb1.yellow_box_x_pos
    yb1.yellow_box_rect.top = yb1.yellow_box_y_pos
    yb2.yellow_box_rect = yb2.yellow_box.get_rect()
    yb2.yellow_box_rect.left = yb2.yellow_box_x_pos
    yb2.yellow_box_rect.top = yb2.yellow_box_y_pos
    yb3.yellow_box_rect = yb3.yellow_box.get_rect()
    yb3.yellow_box_rect.left = yb3.yellow_box_x_pos
    yb3.yellow_box_rect.top = yb3.yellow_box_y_pos
    yb4.yellow_box_rect = yb4.yellow_box.get_rect()
    yb4.yellow_box_rect.left = yb4.yellow_box_x_pos
    yb4.yellow_box_rect.top = yb4.yellow_box_y_pos
    yb5.yellow_box_rect = yb5.yellow_box.get_rect()
    yb5.yellow_box_rect.left = yb5.yellow_box_x_pos
    yb5.yellow_box_rect.top = yb5.yellow_box_y_pos



    
    if character_rect.colliderect(yb1.yellow_box_rect):
        print('충돌했어요.')
        running = False
    if character_rect.colliderect(yb2.yellow_box_rect):
        print('충돌했어요.')
        running = False
    if character_rect.colliderect(yb3.yellow_box_rect):
        print('충돌했어요.')
        running = False
    if character_rect.colliderect(yb4.yellow_box_rect):
        print('충돌했어요.')
        running = False
    if character_rect.colliderect(yb5.yellow_box_rect):
        print('충돌했어요.')
        running = False


    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(yb1.yellow_box, (yb1.yellow_box_x_pos, yb1.yellow_box_y_pos))
    screen.blit(yb2.yellow_box, (yb2.yellow_box_x_pos, yb2.yellow_box_y_pos))
    screen.blit(yb3.yellow_box, (yb3.yellow_box_x_pos, yb3.yellow_box_y_pos))
    screen.blit(yb4.yellow_box, (yb4.yellow_box_x_pos, yb4.yellow_box_y_pos))
    screen.blit(yb5.yellow_box, (yb5.yellow_box_x_pos, yb5.yellow_box_y_pos))

    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))


    # 피한 개수 출력
    avoid_cnt_print = 'you avoided : ' + str(avoid_cnt) 
    screen.blit(game_font.render(str(avoid_cnt_print), True, (255, 255, 255)), (200, 10))

    pygame.display.update()

background = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/run_away_from_yellow_box/background_of_end.png')
screen.blit(background, (0, 0))
pygame.display.update()



collision_msg = game_font.render('you collide to yellow box.', True, (255, 255, 255))
screen.blit(collision_msg,(20, 60))
pygame.display.update()


# currentPath = os.getcwd()
# print(currentPath)
# os.chdir(currentPath)
# files = os.listdir(currentPath)
# print('Files in %r: %s' % (currentPath,files))

# score 파일 읽기 모드로 열기
with open('score.py', 'r', encoding='utf8') as score:
    # 기록된 score 정렬
    total_score = sorted(list(map(int,score.readline().split())))
    # 피한 개수가 누적 기록 최대보다 많으면
    if avoid_cnt >= max(total_score):
        print('최고기록 갱신!')
        total_score_print = game_font.render('you are best player!!', True, (255, 255, 255))
        screen.blit(total_score_print, (20, 140))
    score.close()

# score 파일 읽고쓰기 모드로 열기
with open('score.py', 'a', encoding='utf8') as score:
    score.write(str('{0} '.format(avoid_cnt)))
    score.close()


score_print = game_font.render(str(avoid_cnt_print), True, (255, 255, 255))
screen.blit(score_print, (20, 20))
pygame.display.update()

rank = len(set(total_score)) + 1
for i in set(total_score):
    if avoid_cnt > i:
        rank -= 1
    
rank_print = game_font.render('your rank is -> ' + str(rank) , True, (255, 255, 255))
screen.blit(rank_print, (20, 100))
pygame.display.update()

# screen.blit()
print(avoid_cnt_print)
pygame.time.delay(2500)

# pygame 종료
pygame.quit()