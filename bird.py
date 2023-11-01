from pico2d import *
import random


class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), random.randint(400, 500)
        self.frame = random.randint(0, 4)
        self.action = 2
        self.face_dir = random.choice([1, -1])
        self.dir = 5 if self.face_dir == 1 else -5
        self.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.dir
        self.frame = (self.frame + 1) % 5

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
            self.image.clip_draw(self.frame * (918 // 5) - 2, self.action * (506 // 3) - 2, (918 // 5), (506 // 3),
                                 self.x,
                                 self.y, 100, 100)
        elif self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * (918 // 5) - 2, self.action * (506 // 3) - 2, (918 // 5),
                                           (506 // 3), 0, 'h', self.x,
                                           self.y, 100, 100)
