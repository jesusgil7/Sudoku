from cell import Cell
import pygame
pygame.init()
class Board:
    def __init__(self, width, height, screen, sudoku, solved_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.board = self.initialize_board()
        self.sudoku = sudoku
        self.selected_cell = []
        self.solved_board = solved_board
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

        for row in range(0, len(self.sudoku[0])):  # fill a board with cells
            for col in range(0, len(self.sudoku[0])):
                    self.cells[row][col].draw()
        pygame.display.update()

    def select(self, row, col):
        self.screen.fill((255,255,255))

        cell_surface = pygame.Surface((50, 50))
        cell_surface.fill((135,206,250))
        cell_surface.set_alpha(150)
        cell_rectangle = cell_surface.get_rect(center=(col*50+75,row*50+75))
        self.screen.blit(cell_surface,cell_rectangle)

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
        if self.cells[col][row].get_cell_value() == 0:
            self.selected_cell = [row, col]
            self.select(row, col)

    def clear(self):
        pass

    def sketch(self, value):
        self.cells[self.selected_cell[0]][self.selected_cell[1]].set_sketch_value(value)
        self.cells[self.selected_cell[0]][self.selected_cell[1]].draw()

    def place_number(self):
        sketch_value = self.cells[self.selected_cell[0]][self.selected_cell[1]].get_sketch_value()
        self.cells[self.selected_cell[1]][self.selected_cell[0]].set_cell_value(sketch_value)
        self.sketch(0)
        sketch_value = 0
        self.cells[self.selected_cell[0]][self.selected_cell[1]].draw()
    def reset_to_original(self):
        pass

    def is_full(self):
        counter = 0
        for row in range (0,9):
            for col in range (0,9):
                if self.cells[row][col].get_cell_value() == 0:
                    counter +=1
        if counter != 0:
            return False
        if counter == 0:
            return True

    def updated_board(self):
        pass
    def find_empty(self):
        pass

    def check_board(self):
        for row in range(0, 9):
            for col in range(0, 9):
                if self.cells[row][col].get_cell_value() != self.solved_board[col][row]:
                    return False
        else:
            return True