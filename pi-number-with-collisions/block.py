import pygame
class Block:

    def __init__(self, config: dict):
        w, h = pygame.display.get_surface().get_size() # Refactor: add into config
        ground_offset = 50 # Refactor: add into config

        self.screen = config['screen']
        self.x      = config['x']
        self.y      = h - ground_offset - config['width']
        self.color  = config['color']
        self.width  = config['width']
        self.speed  = config['speed']
        self.mass   = config['mass']

    def update(self):
        self.x = self.x + self.speed

    def hit_wall(self) -> bool:
       return self.x <= 0

    def reverse(self):
        self.speed = self.speed * -1

    def collide(self, other: 'Block') -> bool:
        return not ((self.x + self.width) < other.x) or (self.x > (other.x + other.width))

    def bounce(self, other) -> int:
        sum_mass = self.mass + other.mass
        new_speed = self.speed * ((self.mass - other.mass)/sum_mass) + other.speed * ((2 * other.mass)/sum_mass)
        return new_speed


    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.width)) # Refactor: the draw method could receive a drawer, here the pygame



