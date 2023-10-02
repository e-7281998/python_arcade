import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("파이썬 게임")    #게임 이름

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/전은정/Desktop/Python/python_arcade/pygame_basic/background.png")

# 이벤트 루프
running = True  #게임이 진행중인가?
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   #화면 창의 X 클릭시 발생
            running = False

    screen.blit(background, (0,0))  #1.배경 그리기
    # screen.fill((0,0,255)) #2.배경 채우기
    pygame.display.update() #게임화면을 다시 그리기 : 새 게임마다 계속 그려줘야 함
# pygame 종료
pygame.quit()