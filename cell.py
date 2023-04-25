
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
        self.screen.blit(self.value, ((int(self.col) + 1) * 50 + 15, (int(self.row) + 1) * 50))