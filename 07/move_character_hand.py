from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

# def handle_events():
#     global running
#     global x,y
#     events = get_events()
#
#     for event in events:
#         if event.type == SDL_QUIT:
#             running = False
#         elif event.type == SDL_MOUSEMOTION:
#             x, y = event.x, KPU_HEIGHT - 1 - event.y
#         elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#             running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
hx, hy = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()


def hand_cr():
    global hx, hy
    hx, hy = random.randint(0, 1280), random.randint(0, 1024)


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if x > hx - 10 and x < hx + 10 and y > hy - 10 and y < hy + 10 :
        hand_cr()
    if x > hx:
        x -= 10
    elif x < hx:
        x += 10
    if y > hy:
        y -= 10
    elif y < hy:
        y += 10
    hand.draw(hx, hy)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    # handle_events()

close_canvas()
