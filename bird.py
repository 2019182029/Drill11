from pico2d import *
import random

class Bird:
    def __init__(self):
        self.x, self.y = random.randint(100, 1500), 400
        self.frame = random.randint(0, 4)
        self.action = 2
        self.face_dir = 1
        self.dir = 0
        self.image = load_image('bird_animation.png')


    def update(self):
        self.frame = (self.frame + 1) % 5

        if self.action == 0 and self.frame == 3:
            self.action = 2
            self.frame = 0
        elif self.frame == 4:
            self.action -= 1
            self.frame = 0

        print(self.frame, self.action)

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * (918 // 5) - 2, self.action * (506 // 3) - 2, (918 // 5), (506 // 3), self.x, self.y, 100, 100)
