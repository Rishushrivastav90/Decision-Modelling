import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self, scale_factor):
        super(Bird, self).__init__()
        self.original_img_list = [
            pg.image.load("assets/birdup.png").convert_alpha(),
            pg.image.load("assets/birddown.png").convert_alpha()
        ]
        self.img_list = [pg.transform.scale_by(img, scale_factor) for img in self.original_img_list]
        self.image_index = 0
        self.image = self.img_list[self.image_index]
        self.rect = self.image.get_rect(center=(100, 100))
        self.y_velocity = 0
        self.gravity = 10
        self.flap_speed = 250
        self.anim_counter = 0
        self.update_on = False

    def update(self, dt):
        if self.update_on:
            self.playAnimation()
            self.applyGravity(dt)

            if self.rect.y <= 0 and self.flap_speed == 250:
                self.rect.y = 0
                self.flap_speed = 0
                self.y_velocity = 0
            elif self.rect.y > 0 and self.flap_speed == 0:
                self.flap_speed = 250

    def applyGravity(self, dt):
        self.y_velocity += self.gravity * dt
        self.rect.y += self.y_velocity
    
    def flap(self, dt):
        self.y_velocity = -self.flap_speed * dt

    def playAnimation(self):
        if self.anim_counter == 5:
            self.image = self.img_list[self.image_index]
            self.image_index = 1 - self.image_index  # Toggle between 0 and 1
            self.anim_counter = 0
        self.anim_counter += 1

    def resetPosition(self):
        self.rect.center = (100, 100)
        self.y_velocity = 0
        self.anim_counter = 0

    def scale(self, scale_factor):
        self.img_list = [pg.transform.scale_by(img, scale_factor) for img in self.original_img_list]
        self.image = self.img_list[self.image_index]
        self.rect = self.image.get_rect(center=self.rect.center)