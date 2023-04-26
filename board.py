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
        self.cells = [['-' for col in range(0, len(self.sudoku[0]))] for row in range(0, len(self.sudoku[0]))]

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

        for x in range(0, len(self.sudoku[0])):  # filla board with cells
            for j in range(0, len(self.sudoku[0])):
                if 0 < self.sudoku[x][j] < 10:
                    cellobj = Cell(self.sudoku[x][j], x, j, self.screen)
                    self.cells[x][j] = cellobj
                    cellobj.draw()
        pygame.display.update()
    def select(self, row, col):
        self.screen.fill((255,255,255))

        cell_surface = pygame.Surface((50, 50))
        cell_surface.fill((135,206,250))
        cell_surface.set_alpha(150)
        cell_rectangle = cell_surface.get_rect(center=(col*50+75,row*50+75))
        self.screen.blit(cell_surface,cell_rectangle)
        print(self.sudoku[self.selected_cell[0]][self.selected_cell[1]])

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
        self.selected_cell = [row, col]
        self.select(row,col)

    def clear(self):
        pass

    def sketch(self,value):
        self.sudoku[self.selected_cell[0]][self.selected_cell[1]] = value

    def place_number(self, value):
        self.sudoku[self.selected_cell[0]][self.selected_cell[1]] = value

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