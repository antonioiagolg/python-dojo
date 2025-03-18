class Config:

    def __init__(self):
        self.number_of_digits = 5
        self.timesteps = 30000
        self.mass_tiny_block = 1
        self.mass_bigger_block = self.mass_tiny_block * pow(100, self.number_of_digits - 1)
        self.framerate = 60

        self.blue = (0, 128, 255)
        self.orange = (255, 100, 0)
        self.white = (255, 255, 255)

        self.font = 'Comic Sans MF'
        self.font_size = 30
        self.display_size = (800,600)
