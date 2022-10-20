import pico2d
import play
import title
#running =True
states=[play]#모듈을 변수로

pico2d.open_canvas(1100,600)

for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
        pico2d.delay(0.01)
    state.exit()
# finalization code
pico2d.close_canvas()