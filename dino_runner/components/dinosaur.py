from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, DUCKING, JUMPING
import pygame

class Dinosaur(Sprite):
    
    POS_x = 50
    POS_y = 430
    duck_pos_y = 460
    JUMP_VEL = 8.5
    
    def __init__(self):
        self.Image = RUNNING[0]
        self.rect = self.Image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_y
        self.step_index = 0
        self.runing = True
        self.ducking = False
        self.jumping = False
        self.jump_vel = self.JUMP_VEL
    
    def run(self):
        self.Image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.Image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.POS_y
        self.step_index += 1
    
    def duck(self):
        self.Image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.rect = self.Image.get_rect()
        self.rect.x = self.POS_x
        self.rect.y = self.duck_pos_y
        self.step_index += 1
    
    def jump(self):
        self.Image = JUMPING
        if self.jumping:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.JUMP_VEL:
            self.rect.y = self.POS_y
            self.jumping = False
            self.jump_vel = self.JUMP_VEL
    
    def update(self,user_input):
        if self.jumping:
            self.jump()
        elif self.ducking:
            self.duck()
        elif self.runing:
            self.run()
        
        if user_input[pygame.K_DOWN] and not self.jumping:
            self.runing = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_UP] and not self.jumping:
            self.runing = False
            self.ducking = False
            self.jumping = True
        elif not self.jumping:
            self.runing = True
            self.ducking = False
            self.jumping = False
            
        if self.step_index >= 10:
            self.step_index = 0
            
            
    def draw(self, screen):
        screen.blit(self.Image, self.rect)#dibujar la imagen donde rect