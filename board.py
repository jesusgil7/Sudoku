from cell import Cell
import pygame
pygame.init()
class Board:
    def __init__(self, width, height, screen, difficulty, sudoku):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = self.initialize_board()
        self.sudoku = sudoku
        self.selected_cell = []
        self.cells = [[Cell(self.sudoku[row][col], row, col, self.screen) for row in range(0, len(self.sudoku[0]))] for col in range(0, len(self.sudoku[0]))]

    def initialize_board(self):
        return [["-" for i in range(3)] for j in range(3)]

    def draw(self):
        for i in range(0, 10):
            pygame.draw.line(self.screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)  # draws all vertical lines
            pygame.draw.line(self.screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)  # draws all horizontal lines

            if i % 3 == 0:
                pygame.draw.line(self.screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500),
                                 4)  # draws vertical bold lines surrounding 3x3 cell blocks
                pygame.draw.line(self.screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i),
                                 4)  # draws horizontal bold lines surrounding 3x3 cell blocks
        pygame.display.update()

        for row in range(0, len(self.sudoku[0])):  # filla board with cells
            for col in range(0, len(self.sudoku[0])):
                #if 0 < self.sudoku[col][row] < 10:
                    self.cells[row][col].draw()
        pygame.display.update()
        
    def select(self, row, col):
        self.screen.fill((255,255,255))

        cell_surface = pygame.Surface((50, 50))
        cell_surface.fill((135,206,250))
        cell_surface.set_alpha(150)
        cell_rectangle = cell_surface.get_rect(center=(col*50+75,row*50+75))
        self.screen.blit(cell_surface,cell_rectangle)

        #cellobj.set_cell_value(key)
    def click(self, pos):
        x = pos[0]
        y = pos[1]
        row = 0
        col = 0
        if x > 500 or x < 50 or y > 500 or y <50:
            return None
        else:
            while x > 100:
                x -= 50
                col+=1
            while y > 100:
                y -= 50
                row+=1
        if self.sudoku[row][col] == 0:
            print(row, col)
            print(self.selected_cell)
            self.selected_cell = [row, col]
            print(self.selected_cell)
            self.select(row, col)

    def clear(self):
        pass

    def sketch(self, value):
        self.cells[self.selected_cell[0]][self.selected_cell[1]].set_sketch_value(value)
        self.cells[self.selected_cell[0]][self.selected_cell[1]].draw()

    def place_number(self):
        pass

    def place_number(self, value):
        self.sudoku[self.selected_cell[0]][self.selected_cell[1]] = value
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