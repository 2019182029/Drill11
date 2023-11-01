from pico2d import *
import random
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_SPH = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_SPH * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5
FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(400, 500)
        self.frame = random.randint(0, 4)
        self.action = 2
        self.face_dir = random.choice([1, -1])
        self.dir = 5 if self.face_dir == 1 else -5
        self.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_TIME * game_framework.frame_time) % 5

        if self.x > 1500:
            self.dir = -5
            self.face_dir = -1
        elif self.x < 100:
            self.dir = 5
            self.face_dir = 1

        if self.action == 0 and self.frame == 3:
            self.action, self.frame = 2, 0
        elif self.frame == 4:
            self.action, self.frame = self.action - 1, 0

    def handle_event(self, event):
        pass

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(int(self.frame) * (918 // 5) - 2, self.action * (506 // 3) - 2, (918 // 5), (506 // 3),
                                 self.x,
                                 self.y, 100, 100)
        elif self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame) * (918 // 5) - 2, self.action * (506 // 3) - 2, (918 // 5),
                                           (506 // 3), 0, 'h', self.x,
                                           self.y, 100, 100)
