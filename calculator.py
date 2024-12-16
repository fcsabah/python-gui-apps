import sys

import pygame

pygame.init()

WIDTH, HEIGHT = 400, 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (50, 50, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Calculator")

# font = pygame.font.Font(None, 50)
font = pygame.font.SysFont("bahnschrift", 50)
small_font = pygame.font.Font(None, 40)

BUTTON_WIDTH = 90
BUTTON_HEIGHT = 60
PADDING = 10

current_input = ""
result = None

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]


def draw_buttons():
    for i, row in enumerate(buttons):
        for j, button in enumerate(row):
            x = PADDING + j * (BUTTON_WIDTH + PADDING)
            y = 100 + i * (BUTTON_HEIGHT + PADDING)
            pygame.draw.rect(screen, GRAY, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
            text = font.render(button, True, BLACK)
            screen.blit(text, (
            x + BUTTON_WIDTH // 2 - text.get_width() // 2, y + BUTTON_HEIGHT // 2 - text.get_height() // 2))


def display_input(text):
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, 100))
    rendered_text = font.render(text, True, BLACK)
    screen.blit(rendered_text, (PADDING, 50 - rendered_text.get_height() // 2))


def evaluate_expression(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Error"


def main():
    global current_input, result

    running = True
    while running:
        screen.fill(WHITE)
        display_input(current_input if result is None else result)
        draw_buttons()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                for i, row in enumerate(buttons):
                    for j, button in enumerate(row):
                        btn_x = PADDING + j * (BUTTON_WIDTH + PADDING)
                        btn_y = 100 + i * (BUTTON_HEIGHT + PADDING)
                        if btn_x <= x <= btn_x + BUTTON_WIDTH and btn_y <= y <= btn_y + BUTTON_HEIGHT:
                            if button == "C":
                                current_input = ""
                                result = None
                            elif button == "=":
                                result = evaluate_expression(current_input)
                                current_input = ""
                            else:
                                if result is not None:
                                    result = None
                                    current_input = ""
                                current_input += button


if __name__ == "__main__":
    main()
