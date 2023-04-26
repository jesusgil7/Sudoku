import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch_value = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketch_value(self, value):
        self.sketch_value = value

    def get_cell_value(self):
        return self.value

    def get_sketch_value(self):
        return self.sketch_value

    def draw(self):
        value_font = pygame.font.Font(None, 50)
        sketch_font = pygame.font.Font(None, 20)
        value = value_font.render(str(self.value), True, (0, 0, 0))
        sketch = sketch_font.render(str(self.sketch_value), True, (0, 0, 0))
        value_rect = value.get_rect(center = (self.col * 50 + 150 //2, self.row * 50 + 150 //2))
        sketch_rect = sketch.get_rect(center = (self.row * 50 + 120 // 2, self.col * 50 + 120 // 2))

        if self.sketch_value != 0:
            self.screen.blit(sketch, sketch_rect)
        if self.value != 0:
            self.screen.blit(value, value_rect)