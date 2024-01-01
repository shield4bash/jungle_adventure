import pygame

class map_tile(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        
        self.image = pygame.image.load(f'graphics/map_blocks/{type}.png')
        self.rect = self.image.get_rect(topright = (x,y))


class solid_map_tile(map_tile) :
    def __init__(self, type, x, y):
        super().__init__(type, x, y)




class danger_map_tile(map_tile) :
    def __init__(self, type, x, y):
        super().__init__(type, x, y)





class end_map_tile(map_tile) :
    def __init__(self, type, x, y):
        super().__init__(type, x, y)
