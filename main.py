import pygame
from pygame.locals import *

pygame.init()


BUTTON_WIDTH_RATIO = 0.35
BUTTON_HEIGHT_RATIO = 0.12
BUTTON_SPACING_RATIO = 0.05
BG_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 122, 204)
HIGHLIGHT_COLOR = (0, 149, 0)
EXIT_HIGHLIGHT_COLOR = (255, 20, 20)
SELECTED_COLOR = (34, 139, 34)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 24
SCROLL_COLOR = (220, 220, 220)
SCROLL_SPEED = 5

# Vocabulary data
VOCABULARY = {
    "noha": "leg",
    "sliepka": "chicken",
    "šťastný": "delighted",
    "prestížny": "prestigious",
    "zradca": "traitor",
    "zmrzlina": "ice cream",
    "sníval": "dreamt",
    "ležať": "lay",
    "kráľ": "king",
    "šalat": "lettuce",
    "pôst": "feast",
}


screen = pygame.display.set_mode((800, 600), RESIZABLE)
WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
pygame.display.set_caption("Main Menu")


font = pygame.font.Font(None, FONT_SIZE)

# Prepočítavanie obrazovky
def recalculate_buttons():
    global WINDOW_WIDTH, WINDOW_HEIGHT, button_width, button_height, button_spacing, button_positions
    WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
    button_width = int(WINDOW_WIDTH * BUTTON_WIDTH_RATIO)
    button_height = int(WINDOW_HEIGHT * BUTTON_HEIGHT_RATIO)
    button_spacing = int(WINDOW_HEIGHT * BUTTON_SPACING_RATIO)
    button_positions = {
        "Lesson 1": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 1.5 * button_height - button_spacing),
        "Lesson 2": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 0.5 * button_height),
        "Exit": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 0.5 * button_height + button_spacing)
    }



recalculate_buttons()

# Nastavenia textu
def render_button_text(text, font, button_rect):
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=button_rect.center)
    return text_surface, text_rect

# Tlačidlo (nastavenie parametrov)
def draw_button(screen, text, font, button_rect, is_hovered):
    if text == "Exit":
        color = EXIT_HIGHLIGHT_COLOR if is_hovered else BUTTON_COLOR
    else:
        color = HIGHLIGHT_COLOR if is_hovered else BUTTON_COLOR

    pygame.draw.rect(screen, color, button_rect)
    text_surface, text_rect = render_button_text(text, font, button_rect)
    screen.blit(text_surface, text_rect)


running = True

while running:
    mouse_pos = pygame.mouse.get_pos()
    button_pressed = pygame.mouse.get_pressed()
    button_released = False

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
            recalculate_buttons()

        # keď myška dole
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                button_released = True


    screen.fill(BG_COLOR)

    # Draw butons
    for button_text, position in button_positions.items():
        button_rect = pygame.Rect(position[0], position[1], button_width, button_height)
        is_hovered = button_rect.collidepoint(mouse_pos)

        draw_button(screen, button_text, font, button_rect, is_hovered)

        if is_hovered and button_released:
            if button_text == "Lesson 1":
                print("Lesson 1 clicked")
            elif button_text == "Lesson 2":
                print("Lesson 2 clicked")
            elif button_text == "Exit":
                running = False


    pygame.display.flip()




pygame.quit()


