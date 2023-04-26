import copy
from sudoku_generator import SudokuGenerator, generate_sudoku
from cell import Cell
from board import Board
import pygame

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
            if event.type == pygame.K_RETURN:
                print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    screen.fill(background_color)
                    return generate_sudoku(9, 30)

                elif medium_rectangle.collidepoint(event.pos):
                    screen.fill(background_color)
                    return generate_sudoku(9, 40)

                elif hard_rectangle.collidepoint(event.pos):
                    screen.fill(background_color)
                    return generate_sudoku(9,50)
        pygame.display.update()


def draw_board(screen, sudoku, board): #def draw_board(screen, sudoku, solved, original):
    font = pygame.font.SysFont("arial", 35)
    board.draw()

    # Initialize buttons
    # Initialize text first
    button_font = pygame.font.SysFont("arial", 30) #changed font
    reset_button = button_font.render("Reset", 0, (255,255,255))
    restart_button = button_font.render("Restart", 0, (255,255,255))
    exit_button = button_font.render("Exit", 0, (255,255,255))
    pygame.display.update()

    #same process as menu, buttons for restart, reset, and exit
    reset_surface = pygame.Surface((reset_button.get_size()[0] + 15, reset_button.get_size()[1] + 15))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_button, (10, 10))

    restart_surface = pygame.Surface((restart_button.get_size()[0] + 15, restart_button.get_size()[1] + 15))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_button, (10, 10))

    exit_surface = pygame.Surface((exit_button.get_size()[0] + 15, exit_button.get_size()[1] + 15))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_button, (10, 10))

    reset_rectangle = reset_surface.get_rect(center=(125,525))
    restart_rectangle = restart_surface.get_rect(center=(275, 525))
    exit_rectangle = exit_surface.get_rect(center=(425,525))

    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            key = False
            if event.key == pygame.K_RETURN:
                board.place_number()
                board.draw()
                break
            elif event.key == pygame.K_1:
                key = 1
            elif event.key == pygame.K_2:
                key = 2
            elif event.key == pygame.K_3:
                key = 3
            elif event.key == pygame.K_4:
                key = 4
            elif event.key == pygame.K_5:
                key = 5
            elif event.key == pygame.K_6:
                key = 6
            elif event.key == pygame.K_7:
                key = 7
            elif event.key == pygame.K_8:
                key = 8
            elif event.key == pygame.K_9:
                key = 9

            board.sketch(key)
            board.draw()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if reset_rectangle.collidepoint(event.pos):
                return True

            elif restart_rectangle.collidepoint(event.pos):
                return False

            elif exit_rectangle.collidepoint(event.pos):
                exit()
            board.click(event.pos)
        pygame.display.update()


if __name__ == '__main__':
    game_over = False

    # setting up pygame
    pygame.init()
    pygame.font.init()

    # main menu window
    background_color = (251, 247, 245)
    original_grid_element_color = (52, 31, 151)

    WIDTH = 550
    HEIGHT = 550
    LINE_WIDTH = 15
    WIN_LINE_WIDTH = 15
    BG_COLOR = (255, 255, 245)
    LINE_COLOR = (245, 152, 66)

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    sudoku = draw_game_start(WIN)

    selected_cell = []
    board = Board(500,500, WIN,sudoku)

    while not game_over:
        if draw_board(WIN, sudoku, board) == True:
            WIN.fill(background_color)
            pygame.display.update()
            board = Board(500, 500, WIN, sudoku)
        elif draw_board(WIN, sudoku, board) == False:
            sudoku = draw_game_start(WIN)
            board = Board(500, 500, WIN, sudoku)


