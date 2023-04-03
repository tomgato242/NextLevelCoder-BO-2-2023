import pygame

from dino_runner.utils.constants import BG, CLOUD, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, ICON, LARGE_CACTUS
from dino_runner.components.dinosaur import Dinosaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#Ancho y alto
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 500
        self.posX_cloud = 2000
        self.PosY_cloud = 200
        self.pos_x_cactus = 30
        self.pos_y_cactus = 430
        self.player = Dinosaur()
        

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
    
    def cloud(self):
        imagen= CLOUD.get_width()
        self.screen.blit(CLOUD, (imagen + self.posX_cloud, self.PosY_cloud))
        if self.posX_cloud <= -imagen:
            self.screen.blit(CLOUD, (imagen + self.posX_cloud, self.PosY_cloud))
            self.posX_cloud = 2000
        self.posX_cloud -= self.game_speed
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.cloud()
        self.cactus()
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        
    def cactus(self):
        images= LARGE_CACTUS[0].get_width()
        self.screen.blit(LARGE_CACTUS[0], (images + self.pos_x_cactus, self.pos_y_cactus))
        if self.pos_x_cactus <= -images:
           self.screen.blit(LARGE_CACTUS[0], (images + self.pos_x_cactus, self.pos_y_cactus))
           self.pos_x_cactus = 2500
        self.pos_x_cactus -= self.game_speed

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
