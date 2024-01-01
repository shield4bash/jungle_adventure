import pygame
from sys import exit
import player
from constants import *
from map_tile import *
from game_map import game_map

pygame.init()

screen = pygame.display.set_mode((WORLD_WIDTH,WORLD_HEIGHT))
pygame.display.set_caption('Jungle Adventure')
clock = pygame.time.Clock()

sky_surf = pygame.image.load('graphics/sky.png').convert()



player_group = pygame.sprite.GroupSingle()
player_group.add(player.player())

solid_group = pygame.sprite.Group()
danger_group = pygame.sprite.Group()
end_group = pygame.sprite.Group()


gamem = game_map('map1.csv')

for y, row in enumerate(gamem.read_map_to_array()) :
    for x, block in enumerate(row) :
        if block == '1' or block == '2' :
            solid_group.add(solid_map_tile(MAP_TILE_NUMBER[block], x*MAP_TILE_PIXEL_SIZE, y*MAP_TILE_PIXEL_SIZE))
        elif block == '3' or block == '4' :
            danger_group.add(danger_map_tile(MAP_TILE_NUMBER[block], x*MAP_TILE_PIXEL_SIZE, y*MAP_TILE_PIXEL_SIZE))
        elif block == '5' or block == '6' :
            end_group.add(end_map_tile(MAP_TILE_NUMBER[block], x*MAP_TILE_PIXEL_SIZE, y*MAP_TILE_PIXEL_SIZE))

game_map = [solid_group, danger_group, end_group]

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
    
    screen.blit(sky_surf, (0,0))

    player_group.draw(screen)
    player_group.update(player_group, solid_group)

    for game_tiles in game_map:
        game_tiles.draw(screen)
    
    pygame.display.update()
    clock.tick(60)
    
            