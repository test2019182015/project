import random
from pico2d import *
import pygame
import game_framework
import title
import map_1_state
running = True
frame=0
back_WIDTH, back_HEIGHT = 600, 600
map_state=1
run_move=None
stay_move=0
run_jump=0
move_dir=0
move_to=1
jump_to=0
jump_tr=2
jump_up=1
jump_now_y1=0
jump_now_y2=0
save_x=100
save_y=30
save_map=1
jump_sta=0
map_4_save = 0
ran_s=0
boshy_X=50
boshy_Y=50
boshy_died=False
magazine=None
bul=None
test=[False,False,False]
shot_range=[None,None,None]
shot_X=[None,None,None]
shot_Y=[None,None,None]
shot_to=[None,None,None]
shot_on=0
pygame.mixer.init()
# 710, 896

def map_fir_1_draw():
    # map_1_state.map_fir_1_draw()
    # update_canvas()
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    grass.draw(550, 0,1100,70)

def map_fir_2_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    niddle.draw(340, 60)
    niddle.draw(400, 60)
    niddle.draw(460, 60)
    niddle.draw(520, 60)
    up_block.draw(800, 220)
    up_block.draw(860, 220)
    up_block.draw(920, 380)
    up_block.draw(980, 380)
    up_block.draw(1040, 380)
    up_block.draw(1100, 380)
    grass.draw(350, 0, 800, 70)


def map_fir_3_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    boshy_Y=380
    up_block.draw(0, 380)
    up_block.draw(60, 380)
    up_block.draw(120, 380)
    up_block.draw(180, 380)
    more_jump.draw(500,400,20,20)
    more_jump.draw(650, 400, 20, 20)
    more_jump.draw(800, 400, 20, 20)
    up_block.draw(920, 380)
    up_block.draw(980, 380)
    up_block.draw(1040, 380)
    up_block.draw(1100, 380)


def map_fir_4_draw():
    global map_4_save
    global save_x
    global save_y
    global save_map
    global boshy_X
    global boshy_Y
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    up_block.draw(0, 380)
    up_block.draw(60, 380)
    up_block.draw(120, 380)
    up_block.draw(180, 380)
    up_block.draw(240, 320)
    up_block.draw(300, 320)
    up_block.draw(360, 320)
    if map_state==4:
        pass
        # if 860>bul.shot_now_x+bul.Sh>820and 480>bul.shot_now_y>400:
        #     map_4_save=1
        #     save_x = boshy_X
        #     save_y = boshy_Y
        #     save_map = map_state
        #     print('save')
    if map_4_save==0:
        No_save.draw(860,440,40,40)
    elif map_4_save==1:
        Yes_save.draw(860,440,40,40)

    up_block.draw(860, 380)
    up_block.draw(920, 380)
    up_block.draw(980, 380)
    up_block.draw(1040, 380)
    up_block.draw(1100, 380)
def died():
    global boshy_died
    lol=0
    u=0
    boshy_died=True
    pygame.mixer.music.load('hit_snd.wav')
    pygame.mixer.music.play()
    delay(0.5)
    pygame.mixer.music.pause()
    pygame.mixer.music.load('loludied.mp3')
    pygame.mixer.music.play()
    while boshy_died==True:
        draw_back()
        gameOver.draw(500,300,400+lol,400+lol)
        handle_events()
        if lol<=100 and u==0:
            lol+=5
            if lol>100:
                u=1
        elif lol>=0 and u==1:
            lol-=5
            if lol<0:
                u=0
        delay(0.01)
        update_canvas()



def draw_back():
    move_map()
    if map_state==1:
       map_fir_1_draw()
    elif map_state==2:
        map_fir_2_draw()
    elif map_state==3:
        map_fir_3_draw()
    elif map_state==4:
        map_fir_4_draw()
def move_map():
    global map_state
    global boshy_X
    global boshy_Y
    if (boshy_X > 1100 and map_state == 1):
        map_state = 2
        boshy_X = 10
        boshy_Y = 380
    if (boshy_X < 0 and map_state == 2):
        map_state = 1
        boshy_X = 1090
        boshy_Y = 380
    if (boshy_X > 1100 and map_state == 2):
        map_state = 3
        boshy_X = 10
    if (boshy_X < 0 and map_state == 3):
        map_state = 2
        boshy_X = 1090
        boshy_Y = 380
    if (boshy_X > 1100 and map_state == 3):
        map_state = 4
        boshy_X = 10
    if (boshy_X < 0 and map_state == 4):
        map_state = 3
        boshy_X = 1090


def run_draw_move():
    global frame
    global boshy_X
    global boshy_Y
    draw_back()
    if move_to == 0: #left run
        character.clip_draw(frame * 128, 1280, 128, 130, boshy_X, boshy_Y, 30, 30)
        boshy_X+=move_dir*7

        frame = (frame + 1) % 6
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
    elif move_to == 1: #right run
        character.clip_draw(frame * 128, 1280, 128, 130, boshy_X, boshy_Y, 30, 30)
        boshy_X += move_dir*7

        frame = (frame + 1) % 6+6
    handle_events()


def stay_draw():
    global frame
    global boshy_X
    global boshy_Y
    draw_back()
    if move_to == 0:  # left run
        frame = 1
        character.clip_draw(frame * 128, 1280, 128, 130,boshy_X, boshy_Y, 30, 30)
        update_canvas()
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
    elif move_to == 1:  # right run
        frame = 7
        character.clip_draw(frame * 128, 1280, 128, 130, boshy_X, boshy_Y, 30, 30)
        update_canvas()
    handle_events()
def run_draw_up():
    global frame
    global move_to
    global jump_up
    global jump_sta
    global jump_tr
    global run_jump
    global boshy_X
    global boshy_Y
    draw_back()
    handle_events()
    boshy_Y = boshy_Y + jump_up
    if(boshy_Y < jump_now_y1 + 120):
        if move_to == 0:  # left run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_X, boshy_Y, 30, 30)
            frame = (frame + 1) % 6
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
        elif move_to == 1:  # right run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_X, boshy_Y, 30, 30)
            frame = (frame + 1) % 6 + 6
    elif boshy_Y > jump_now_y1 + 120:
        jump_up=-10
    if boshy_Y<=jump_now_y2:
        jump_up = 0
        jump_tr=2
        run_jump = 0

def run():
    if run_move == 1:
        run_draw_move()
    if stay_move == 1:
        stay_draw()
def start_run():
    global frame,magazine,shot_on
    global boshy_X
    global boshy_Y
    draw_back()
    frame = 7
    character.clip_draw(frame * 128, 1280, 128, 130, boshy_X, boshy_Y, 30, 30)
    update_canvas()
def handle_events():
     global running
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             running = False
         elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                press_key_right()
            if event.key == SDLK_LEFT:
                press_key_left()
            if event.key == SDLK_UP:
                press_key_up()
            if event.key == SDLK_x:
                prass_key_x()
            if event.key == SDLK_r:
                prass_key_r()
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(title)
                running=False
         elif event.type == SDL_KEYUP:
              if event.key == SDLK_RIGHT:
                  up_key_right()
              elif event.key == SDLK_LEFT:
                  up_key_left()


def press_key_right():
    global stay_move, run_move, move_to, move_dir
    stay_move = 0
    run_move = 1
    move_to = 1
    move_dir += 1
    run()


def press_key_left():
    global stay_move, run_move, move_to, move_dir
    stay_move = 0
    run_move = 1
    move_to = 0
    move_dir -= 1
    run()


def press_key_up():
    global jump_up, jump_sta, jump_tr, jump_now_y1, jump_now_y2, stay_move, run_jump
    if jump_tr > 0:
        if jump_tr == 2:
            jump_now_y2 = boshy_Y
        jump_up = 10
        jump_sta = 0
        jump_tr -= 1
        jump_now_y1 = boshy_Y
        stay_move = 0
        run_jump = 1


def up_key_left():
    global move_dir, run_move, stay_move
    move_dir += 1
    run_move = 0
    stay_move = 1
    run()


def up_key_right():
    global move_dir, run_move, stay_move
    move_dir -= 1
    run_move = 0
    stay_move = 1
    run()


def prass_key_r():
    global boshy_Y
    global boshy_X
    global ran_s, map_state
    boshy_died=False
    ran_s = random.randint(1, 6)
    boshy_X = save_x
    boshy_Y = save_y
    map_state = save_map
    pygame.mixer.music.pause()
    pygame.mixer.music.load('its_snd.wav')
    pygame.mixer.music.play()
    delay(0.5)
    print('load')
    if ran_s == 1:
        pygame.mixer.music.load('boshy4_snd.wav')
        pygame.mixer.music.play()
    elif ran_s == 2:
        pygame.mixer.music.load('boshy4_snd.wav')
        pygame.mixer.music.play()
    elif ran_s == 3:
        pygame.mixer.music.load('boshy4_snd.wav')
        pygame.mixer.music.play()
    elif ran_s == 4:
        pygame.mixer.music.load('boshy4_snd.wav')
        pygame.mixer.music.play()
    elif ran_s == 5:
        pygame.mixer.music.load('boshy4_snd.wav')
        pygame.mixer.music.play()
    elif ran_s == 6:
        pygame.mixer.music.load('boshy4_snd.wav')
        pygame.mixer.music.play()
    delay(0.5)
    # pygame.mixer.music.load('time_snd.wav')
    # pygame.mixer.music.play()

def prass_key_x():
    global shot_on
    global move_to
    shot_on+=1
    shOt()



def shOt():
    global test,shot_Y,shot_X,shot_to,shot_range
    for i in range(0,3,1):
        if(test[i]==False):
            test[i]=True
            shot_Y[i]=boshy_Y
            shot_X[i]=boshy_X
            if move_to==1:
                shot_to[i]=move_to
                shot_range[i]=shot_X[i]+800
            elif move_to==0:
                shot_to[i] = move_to
                shot_range[i] = shot_X[i] - 800
            break


def shot():
    global test, shot_Y, shot_X, shot_to, shot_range
    for i in range(0, 3, 1):
        if (test[i] == True):
            bullet.draw(shot_X[i],shot_Y[i],15,15)
            if shot_to[i]==1:
                shot_X[i]=shot_X[i]+10
                if shot_X[i]>=shot_range[i]:
                    test[i]=False
                    shot_X[i]=None
                    shot_Y[i]=None
                    shot_to[i]=None
                    shot_range[i]=None
            elif shot_to[i]==0:
                shot_X[i]=shot_X[i]-10
                if shot_X[i]<=shot_range[i]:
                    test[i]=False
                    shot_X[i]=None
                    shot_Y[i]=None
                    shot_to[i]=None
                    shot_range[i]=None


def draw():
    draw_back()
    character.clip_draw(frame * 128, 1280, 128, 130, boshy_X, boshy_Y, 30, 30)
    run()
    if run_jump > 0 and jump_tr>=0:
        run_draw_up()
    shot()
    update_canvas()
def update():
    pass

def exit():
    global grass,map_1,map_2,map_3,map_4,map_5,character,up_block,niddle,more_jump,Yes_save,No_save,gameOver
    # del grass,map_1,map_2,map_3,map_4,map_5,character,up_block,niddle,more_jump,Yes_save,No_save,gameOver
    pass

grass=None
map_1=None
map_2=None
map_3=None
map_4=None
map_5=None
character=None
up_block=None
niddle=None
more_jump=None
Yes_save=None
No_save=None
gameOver=None
bullet=None
def enter():
    global grass, map_1, map_2, map_3, map_4, map_5, character, up_block, niddle, more_jump, Yes_save, No_save, gameOver,bullet
    grass = load_image('grass1.png')
    map_1 = load_image('map_1.png')
    map_2 = load_image('map_2.png')
    map_3 = load_image('map_3.png')
    map_4 = load_image('map_4.png')
    map_5 = load_image('map_5.png')
    character = load_image('bosh.png')
    up_block = load_image('up_block.png')
    niddle = load_image('niddle_test.png')
    more_jump = load_image('more_jump.png')
    Yes_save = load_image('Yes_save.png')
    No_save = load_image('No_save.png')
    gameOver = load_image('GameOver.png')
    bullet=load_image('bullet.png')
    start_run()
    map_1_state.enter()

# enter()
# open_canvas(back_WIDTH+500, back_HEIGHT)
# start_run()
# while running:
#     draw()
#     handle_events()
#     update_canvas()
#     delay(0.01)
# close_canvas()




