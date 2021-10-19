import random

from pico2d import *


# Game object class here


class Grass:
    def __init__(self):  # 생성자
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    pass


class Character:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100, 700)
        self.y = 90  # random.randint(90,200)
        self.frame = random.randint(0, 7)

    def update(self):
        self.x += random.randint(2, 10)
        self.frame = (self.frame + 1) % 8
        if self.x >= 800:
            self.x = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class smallBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(100, 700)
        self.y = 599
        self.speed = random.randint(3,10)

    def update(self):
        self.y -= self.speed
        if self.y <= 60:
            self.y = 60;

    def draw(self):
        self.image.draw(self.x, self.y)


class bigBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(100, 700)
        self.y = 599
        self.speed = random.randint(3, 10)

    def update(self):
        self.y -= self.speed
        if self.y <= 70:
            self.y = 70;

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


# initialization code


open_canvas()

grass = Grass()
#sball = smallBall()
#bball = bigBall()
team = [Character() for i in range(11)]
sballgroup = [smallBall() for i in range(10)]
bballgroup = [bigBall() for i in range(10)]
running = True

# game main loop code

while running:
    delay(0.05)
    handle_events()

    # Game logic
    for Character in team:
        Character.update()
    for smallBall in sballgroup:
        smallBall.update()
    for bigBall in bballgroup:
        bigBall.update()
    # Game drawing
    clear_canvas()

    for smallBall in sballgroup:
        smallBall.draw()
    for bigBall in bballgroup:
        bigBall.draw()

    grass.draw()

    for Character in team:
        Character.draw()
    update_canvas()

# finalization code
