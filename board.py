import pygame
pygame.init()
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.initialize_board()

    def initialize_board(self):
        return [["-" for i in range(3)] for j in range(3)]

    def draw(self):
        pass
    def select(self, row, col):
        cell_surface = pygame.Surface((50, 50))
        cell_surface.fill((135,206,250))
        cell_surface.set_alpha(150)
        cell_rectangle = cell_surface.get_rect(center=(row*50+75,col*50+75))
        self.screen.blit(cell_surface,cell_rectangle)

    def click(self, pos):
        x = pos[0]
        y = pos[1]
        counterx = 0
        countery = 0
        if x > 500 or x < 50 or y > 500 or y <50:
            return None
        else:
            while x> 100:
                x -= 50
                counterx+=1
            while y > 100:
                y -= 50
                countery+=1
            self.select(counterx,countery)

    def clear(self):
        pass

    def sketch(self):
        pass

    def place_number(self):
        pass

    def place_number(self):
        pass
    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def updated_board(self):
        pass
    def find_empty(self):
        pass

    def check_board(self):
        pass