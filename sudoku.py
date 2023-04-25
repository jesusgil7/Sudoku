import copy
from sudoku_generator import SudokuGenerator, generate_sudoku

# setting up pygame

import pygame
pygame.init()
pygame.font.init()

background_color = (251, 247, 245)
original_grid_element_color = (52, 31, 151)


WIDTH = 550
HEIGHT = 550
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BG_COLOR = (255, 255, 245)
LINE_COLOR = (245, 152, 66)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_game_start(screen):
    # Initialize title font
    start_title_font = pygame.font.SysFont("arial", 100)
    button_font = pygame.font.SysFont("arial", 70)

    # Color background
    screen.fill(BG_COLOR)

    # Initialize and draw title
    title_surface = start_title_font.render("Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    # Initialize buttons
    # Initialize text first
    easy_button = button_font.render("Easy", 0, (255, 255, 255))
    medium_button = button_font.render("Medium", 0, (255, 255, 255))
    hard_button = button_font.render("Hard", 0, (255, 255, 255))

    # Initialize button background color and text
    easy_surface = pygame.Surface((easy_button.get_size()[0] + 20, easy_button.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_button, (10, 10))
    medium_surface = pygame.Surface((medium_button.get_size()[0] + 20, medium_button.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_button, (10, 10))
    hard_surface = pygame.Surface((hard_button.get_size()[0] + 20, hard_button.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_button, (10, 10))

    # Initialize button rectangle
    easy_rectangle = easy_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25))
    medium_rectangle = medium_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 125))
    hard_rectangle = hard_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 225))

    # Draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    screen.fill(background_color)
                    #return generate_sudoku(9, 30)
                    #return draw_board(WIN, generate_sudoku(9, 40))
                    sudoku = generate_sudoku(9,30)
                    draw_board(WIN, sudoku)

                elif medium_rectangle.collidepoint(event.pos):
                    screen.fill(background_color)
                    #return generate_sudoku(9, 40)
                    draw_board(WIN, generate_sudoku(9,40))

                elif hard_rectangle.collidepoint(event.pos):
                    screen.fill(background_color)
                    #return generate_sudoku(9, 50)
                    draw_board(WIN, generate_sudoku(9,50))

        pygame.display.update()


def draw_board(screen, sudoku): #def draw_board(screen, sudoku, solved, original):
    font = pygame.font.SysFont("arial", 35)

    for i in range(0, 10):
        pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 2)  # draws all vertical lines
        pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 2)  # draws all horizontal lines

        if i % 3 == 0:
            pygame.draw.line(screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4) #draws vertical bold lines surrounding 3x3 cell blocks
            pygame.draw.line(screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4) #draws horizontal bold lines surrounding 3x3 cell blocks
    pygame.display.update()


    for x in range(0, len(sudoku[0])):                      #filla board with cells
        for j in range(0, len(sudoku[0])):
            if 0 < sudoku[x][j] < 10:
                value = font.render(str(sudoku[x][j]), True, (0, 0, 0))
                screen.blit(value, ((j + 1) * 50 + 15, (x + 1) * 50))

    '''
    for x in range(0, len(sudoku[0])):                      #filla board with cells
        for j in range(0, len(sudoku[0])):
            if 0 < sudoku[x][j] < 10:
                cellobj = Cell(sudoku[x][j], x, j, WIN)
                cellobj.draw()
    pygame.display.update()
    '''

    # Initialize buttons
    # Initialize text first
    button_font = pygame.font.SysFont("arial", 30) #changed font
    reset_button = button_font.render("Reset", 0, (255, 255, 255))
    restart_button = button_font.render("Restart", 0, (255, 255, 255))
    exit_button = button_font.render("Exit", 0, (255, 255, 255))

    reset_surface = pygame.Surface((reset_button.get_size()[0] + 15, reset_button.get_size()[1] + 15))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_button, (10, 10))

    restart_surface = pygame.Surface((restart_button.get_size()[0] + 15, restart_button.get_size()[1] + 15))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_button, (10, 10))

    exit_surface = pygame.Surface((exit_button.get_size()[0] + 15, exit_button.get_size()[1] + 15))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_button, (10, 10))

draw_game_start(WIN)