from pico2d import *
import play
import game_framework
running=True
logo=None
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN:
            if event.key == pico2d.SDLK_SPACE:
                game_framework.change_state(play)
                running=False
            elif (event.key)==(SDLK_ESCAPE):
                game_framework.quit()
def draw():
    clear_canvas()
    logo.draw(550,300,1100,600)
    update_canvas()

def enter():
    global logo
    global running
    running = True
    logo=load_image('logo.png')
    pass
def exit():
    global logo
    del logo
    pass


def update():
    pass
