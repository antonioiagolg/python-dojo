import pygame
from block import Block
from config import Config


class Main:

    def __init__(self, config):
        pygame.init()
        pygame.font.init()

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(config.font, config.font_size)
        self.screen = pygame.display.set_mode(config.display_size)
        self.bounce_count = 0
        self.config = config

        self.small_block = Block({
            'screen': self.screen,
            'x': 100,
            'width': 20,
            'speed': 0,
            'mass': config.mass_tiny_block,
            'color': config.blue
        })

        self.big_block = Block({
            'screen': self.screen,
            'x': 200,
            'width': 150,
            'speed': -0.00005,
            'mass': config.mass_bigger_block,
            'color': config.orange
        })

        self.done = False

    def draw(self):
        for _ in range(self.config.timesteps): # Refactor: remove update actions to another function
            if self.small_block.hit_wall():
                self.small_block.reverse()
                self.bounce_count += 1

            if self.small_block.collide(self.big_block):
                speed_small_block = self.small_block.bounce(self.big_block)
                speed_big_block   = self.big_block.bounce(self.small_block)

                self.small_block.speed = speed_small_block
                self.big_block.speed = speed_big_block

                self.bounce_count += 1

            self.small_block.update()
            self.big_block.update()

        self.small_block.draw()
        self.big_block.draw()

    def show_GUI(self):
        pi_text = self.font.render(f"PI equals: {self.bounce_count}", False, self.config.white)
        digits_text = self.font.render(f"Number of digits: {self.config.number_of_digits}", False, self.config.white)
        self.screen.blit(pi_text, (10,10))
        self.screen.blit(digits_text, (10,40))

        
    def start(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            self.screen.fill((0,0,0))
            self.draw()
            self.show_GUI()
            pygame.display.flip()
            self.clock.tick(self.config.framerate)


if __name__ == "__main__":
    Main(Config()).start()
