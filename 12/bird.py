import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (100.0 / 0.33)  # 100 pixel 40 cm ///새의 이미지 크기 100px 멧비둘기의 평균 몸길이 33cm
RUN_SPEED_KMPH = 123.0  # Km / Hour/// 비둘기 평속 123km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


class Bird:
    image_1 = None
    image_2 = None

    def __init__(self):
        if Bird.image_1 == None:
            Bird.image_1 = load_image('bird100x100x14.png')
        if Bird.image_2 == None:
            Bird.image_2 = load_image('bird100x100x14_1.png')
        self.x, self.y = random.randint(50, 1600 - 50), random.randint(90 + 50, 600 - 50)
        self.velocity = 1
        self.frame = random.randint(0, 14 - 1)
        self.timer = 0
        self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image_1.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        else:
            self.image_2.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # fill here for draw

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.timer = (self.timer + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 10
        if self.timer < 1:
            self.dir *= -1
        if self.x <= 50:
            self.dir = 1
        if self.x >= 1550:
            self.dir = -1
        self.velocity = self.dir * RUN_SPEED_PPS
        self.x += self.velocity * game_framework.frame_time
