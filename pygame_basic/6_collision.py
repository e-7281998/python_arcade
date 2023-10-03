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
background = pygame.image.load("./image/background.png")

# 캐릭터 불러오기
character = pygame.image.load("./image/character.png")
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

# 적 enermy 캐릭터
enermy = pygame.image.load("./image/enermy.png")
enermy_size = character.get_rect().size #이미지의 크기 구해옴 :get_rect() => 사각형의 size
enermy_width = character_size[0] #캐릭터의 가로크기
enermy_height = character_size[1]   #캐릭터의 세로크기
enermy_x_pos = (screen_width / 2) - (enermy_width / 2)#화면 가로의 절반 크기에 해당하는 곳에 위치
enermy_y_pos = (screen_height / 2) - (enermy_height / 2)  #화면 세로의 가장 아래에

# 이벤트 루프
running = True  #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수 설정 : 초당 n번 띄움

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

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    # 캐릭터가 움직여도 rect정보는 같음. 움직일때 화면상의 정보와 같이 변경해줘야 함.
    # print("character_rect : " , character_rect)
    character_rect.left = character_x_pos
    character_rect.right = character_y_pos

    enermy_rect = enermy.get_rect()
    enermy_rect.left = enermy_x_pos
    enermy_rect.right = enermy_y_pos

    # 충돌 체크
    # colliderect : 사각형 기준으로 충돌이 있었는지 확인하는 함수
    # character_rect가 enermy_rect와 충돌을 했느냐?
    if character_rect.colliderect(enermy_rect):
        print("충돌했음")
        running = False

    screen.blit(background, (0,0))  #배경 그리기
    screen.blit(character, (character_x_pos , character_y_pos))

    screen.blit(enermy, (enermy_x_pos, enermy_y_pos)) #적 그리기

    pygame.display.update() #게임화면을 다시 그리기 : 새 게임마다 계속 그려줘야 함
# pygame 종료
pygame.quit()