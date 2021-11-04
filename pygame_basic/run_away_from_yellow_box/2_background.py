import pygame
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption('frants game') #게임 이름

# 배경 이미지 불러오기
backgrond = pygame.image.load('C:/Users/종환PC/Desktop/pygame_basic/background.png')

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님
            
    screen.blit(backgrond, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()