import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketch_value(self,value):
        self.sketch_value = value

    def draw(self):
        chip_font = pygame.font.Font(None, 50)
        chip = chip_font.render(str(self.value), True, (0, 0, 0))
        chip_rect = chip.get_rect(center = (self.col * 50 + 150 //2, self.row * 50 + 150 //2))
        self.screen.blit(chip, chip_rect)