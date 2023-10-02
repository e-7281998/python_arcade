import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("파이썬 게임")    #게임 이름

#FPS
clock = pygame.time.Clock()

# 배경이미지 불러오기
background = pygame.image.load("C:/Users/전은정/Desktop/Python/python_arcade/pygame_basic/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/Users/전은정/Desktop/Python/python_arcade/pygame_basic/character.png")
character_size = character.get_rect().size #이미지의 크기 구해옴 :get_rect() => 사각형의 size
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1]   #캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)#화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height  #화면 세로의 가장 아래에

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True  #게임이 진행중인가?
while running:
    dt = clock.tick(10) #게임화면의 초당 프레임 수 설정 : 초당 n번 띄움

    # 프레임수가 달라진다고해서 게임 속도가 달라지면 안됨!!!
    # 캐릭터가 1초동안 100만큼 이동해야한다면
    # 10 fps : 1초 동안 10번 동작 -> 1번에 10만큼 이동해야 함 : 10 * 10 = 100
    # 20 fps : 1초 동안 20번 동작 -> 1번에 5만큼 이동해야 함 : 20 * 5 = 100
    # print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get():    #어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:   #화면 창의 X 클릭시 발생
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계 처리
    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width  - character_width :
        character_x_pos = screen_width - character_width

    # 세로 경계 처리
    if character_y_pos < 0 :
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height :
        character_y_pos = screen_height - character_height

    screen.blit(background, (0,0))  #배경 그리기
    screen.blit(character, (character_x_pos , character_y_pos))

    pygame.display.update() #게임화면을 다시 그리기 : 새 게임마다 계속 그려줘야 함
# pygame 종료
pygame.quit()