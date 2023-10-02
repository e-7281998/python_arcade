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

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/전은정/Desktop/Python/python_arcade/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기 구해옴 :get_rect() => 사각형의 size
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1]   #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)#화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  #화면 세로의 가장 아래에

# 이벤트 루프
running = True  #게임이 진행중인가?
while running:
    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   #화면 창의 X 클릭시 발생
            running = False

    screen.blit(background, (0,0))  #배경 그리기
    screen.blit(character, (character_x_pos , character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기 : 새 게임마다 계속 그려줘야 함
# pygame 종료
pygame.quit()