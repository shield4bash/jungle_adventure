import pygame
from constants import *

class player(pygame.sprite.Sprite) :
    def __init__(self) :
        super().__init__()

        player_walk_1 = pygame.image.load('graphics/player/adventure_boy_walk_1.png')
        player_walk_2 = pygame.image.load('graphics/player/adventure_boy_walk_2.png')

        self.walking_frames = [player_walk_1, player_walk_2]
        self.frame_index = 0

        self.image = self.walking_frames[self.frame_index]
        self.rect = self.image.get_rect(center = (WORLD_WIDTH/2, WORLD_HEIGHT/2))

    def move_animation(self) :
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_d] :
            self.frame_index += 0.1    
            if self.frame_index >= len(self.walking_frames) : self.frame_index = 0
            self.image = self.walking_frames[int(self.frame_index)]
            
            if keys[pygame.K_a] :
                self.rect.x -= PLAYER_SPEED
            else :
                self.rect.x += PLAYER_SPEED
            
        else :
            self.image = pygame.image.load('graphics/player/adventure_boy_standing.png')

        if keys[pygame.K_SPACE] :
            self.image = pygame.image.load('graphics/player/adventure_boy_jump.png')
            self.rect.y -= PLAYER_JUMP_HEIGHT
    
    def appy_gravity(self) :
        self.rect.y += GRAVITY


    def apply_collisions(self, player_group, solid_group) :
        while pygame.sprite.spritecollide(player_group.sprite, solid_group, False) :
            self.rect.y -= 2


    def update(self, player_group, solid_group) :
        self.move_animation()
        self.appy_gravity()
        self.apply_collisions(player_group, solid_group)

        if self.rect.bottom > WORLD_HEIGHT :
            self.rect.bottom = 0
