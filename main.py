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
FONT_SIZE_2 = 36
SCROLL_COLOR = (220, 220, 220)
SCROLL_SPEED = 5

VOCABULARY_1 = {
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
    "ryba": "fish",
    "macka": "cat",
    "mniška": "nun",
    "1": "one",
    "hodina": "hour",
    "cukor": "sugar",
    "list": "leaf",
    "mrkva": "carrot",
    "dodávka": "lorry",
    "kačka": "duck",
    "líška": "fox",
    "prši": "it's raining",
    "sedieť": "sit",
    "pád": "fall",
    "koruna": "crown",
    "zima": "winter",
    "pozemok": "parcel",
    "krab": "crab",
    "tráva": "grass",
}

VOCABULARY_2 = {
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
    "ryba": "fish",
    "macka": "cat",
    "mniška": "nun",
    "1": "one",
    "hodina": "hour",
    "cukor": "sugar",
    "list": "leaf",
    "mrkva": "carrot",
    "dodávka": "lorry",
    "kačka": "duck",
    "líška": "fox",
    "prši": "it's raining",
    "sedieť": "sit",
    "pád": "fall",
    "koruna": "crown",
    "zima": "winter",
    "pozemok": "parcel",
    "krab": "crab",
    "tráva": "grass",
}

screen = pygame.display.set_mode((800, 600), RESIZABLE)
WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
pygame.display.set_caption("Main Menu")

font = pygame.font.Font(None, FONT_SIZE)
font_hedings = pygame.font.Font(None, FONT_SIZE_2)


def recalculate_buttons():
    global WINDOW_WIDTH, WINDOW_HEIGHT, button_width, button_height, button_spacing, button_positions
    WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
    button_width = int(WINDOW_WIDTH * BUTTON_WIDTH_RATIO)
    button_height = int(WINDOW_HEIGHT * BUTTON_HEIGHT_RATIO)
    button_spacing = int(WINDOW_HEIGHT * BUTTON_SPACING_RATIO)
    button_positions = {
        "MAIN MENU": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 4 * button_height - button_spacing),
        "Lesson 1": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 1.5 * button_height - button_spacing),
        "Lesson 2": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 0.5 * button_height),
        "Exit": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 0.5 * button_height + button_spacing)
    }


recalculate_buttons()


def render_button_text(text, font, button_rect, font_hedings):
    if text in ("LESSON 1", "LESSON 2", "MAIN MENU"):
        text_surface = font_hedings.render(text, True, (0, 0, 0))
    else:
        text_surface = font.render(text, True, TEXT_COLOR)

    text_rect = text_surface.get_rect(center=button_rect.center)
    return text_surface, text_rect


def draw_button(screen, text, font, button_rect, is_hovered):
    if text == "Exit":
        color = EXIT_HIGHLIGHT_COLOR if is_hovered else BUTTON_COLOR
    elif text in ("LESSON 1", "LESSON 2", "MAIN MENU"):
        color = (255, 255, 255)
    else:
        color = HIGHLIGHT_COLOR if is_hovered else BUTTON_COLOR

    pygame.draw.rect(screen, color, button_rect)
    text_surface, text_rect = render_button_text(text, font, button_rect, font_hedings)
    screen.blit(text_surface, text_rect)


def lesson_1_menu():
    pygame.display.set_caption("Lesson 1")
    global screen
    lesson_running = True
    while lesson_running:
        mouse_pos = pygame.mouse.get_pos()
        button_pressed = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                lesson_running = False

            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True

        screen.fill(BG_COLOR)

        button_width = int(WINDOW_WIDTH * BUTTON_WIDTH_RATIO)
        button_height = int(WINDOW_HEIGHT * BUTTON_HEIGHT_RATIO)
        button_spacing = int(WINDOW_HEIGHT * BUTTON_SPACING_RATIO)

        lesson_buttons = {
            "LESSON 1": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 4 * button_height - button_spacing),
            "Vocabulary": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 1.5 * button_height - button_spacing),
            "Reading": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 0.5 * button_height),
            "Grammar": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 0.5 * button_height + button_spacing),
            "Exit": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 1.5 * button_height + 2 * button_spacing)
        }

        for button_text, position in lesson_buttons.items():
            button_rect = pygame.Rect(position[0], position[1], button_width, button_height)
            is_hovered = button_rect.collidepoint(mouse_pos)

            draw_button(screen, button_text, font, button_rect, is_hovered)

            if is_hovered and button_released:
                if button_text == "Exit":
                    lesson_running = False

                elif button_text == "Reading":
                    print("Reading 1 clicked")
                    reading_1_section()
                    pygame.display.set_caption("Lesson 1")

                elif button_text == "Vocabulary":
                    print("Vocabulary 1 clicked")
                    vocabulary_1_section()
                    pygame.display.set_caption("Lesson 1")

                elif button_text == "Grammar":
                    print("Grammar 1 clicked")
                    grammar_1_section()
                    pygame.display.set_caption("Lesson 1")

                else:
                    print(f"{button_text} clicked in Lesson 1!")

        pygame.display.flip()


def vocabulary_1_section():
    pygame.display.set_caption("Lesson 1 Vocabulary")
    global screen
    scroll_y = 0
    running = True

    user_inputs = {word: "" for word in VOCABULARY_1}
    vocab_height = len(VOCABULARY_1) * (FONT_SIZE + 20)
    active_input = None

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True
                elif event.button == 4:
                    scroll_y = min(scroll_y + SCROLL_SPEED, 0)
                elif event.button == 5:
                    scroll_y = max(scroll_y - SCROLL_SPEED, -vocab_height + WINDOW_HEIGHT)

                for word, input_rect in input_boxes:
                    if input_rect.collidepoint(mouse_pos):
                        active_input = word
                        break
                else:
                    active_input = None



            elif event.type == KEYDOWN and active_input is not None:
                if event.key == K_BACKSPACE:
                    user_inputs[active_input] = user_inputs[active_input][:-1]
                else:
                    user_inputs[active_input] += event.unicode

        screen.fill(BG_COLOR)

        y = scroll_y
        input_boxes = []

        for word in VOCABULARY_1:
            word_surface = font.render(word, True, (0, 0, 0))
            screen.blit(word_surface, (20, y))

            input_rect = pygame.Rect(200, y, 200, FONT_SIZE + 10)
            pygame.draw.rect(
                screen,
                (255, 255, 0) if active_input == word else (200, 200, 200),
                input_rect,
            )

            input_text_surface = font.render(user_inputs[word], True, (0, 0, 0))
            screen.blit(input_text_surface, (input_rect.x + 5, input_rect.y + 5))

            input_boxes.append((word, input_rect))
            y += FONT_SIZE + 20

        check_button = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 50, 100, 40)
        if check_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, check_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, check_button)
        check_text, check_text_rect = render_button_text("Check", font, check_button, font_hedings)
        screen.blit(check_text, check_text_rect)

        exit_button = pygame.Rect(20, WINDOW_HEIGHT - 50, 100, 40)
        if exit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, EXIT_HIGHLIGHT_COLOR, exit_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        exit_text, exit_text_rect = render_button_text("Exit", font, exit_button, font_hedings)
        screen.blit(exit_text, exit_text_rect)

        if exit_button.collidepoint(mouse_pos) and button_released:
            running = False

        if check_button.collidepoint(mouse_pos) and button_released:
            for word, correct_translation in VOCABULARY_1.items():
                if user_inputs[word].strip().lower() == correct_translation:
                    print(f"{word}: Correct")
                else:
                    print(f"{word}: Incorrect")

        pygame.display.flip()


def reading_1_section():
    pygame.display.set_caption("Lesson 1 Reading")
    global screen  # Use the global screen variable
    scroll_y = 0
    running = True

    content = [
        "This is a sample text for the reading section.",
        "You can add multiple lines to test the scrollable feature.",
        "Each line of text can represent a paragraph in your lesson.",
        "Feel free to expand this to fit your requirements.",
        "Scroll down to see more content.",
    ]

    questions = [
        {"text": "Question 1: Is this a sample question?", "true_rect": None, "false_rect": None, "answer": True},
        {"text": "Question 2: Does scrolling work?", "true_rect": None, "false_rect": None, "answer": True},
        {"text": "Question 3: Is this section interactive?", "true_rect": None, "false_rect": None, "answer": True},
    ]

    user_answers = [None] * len(questions)
    content_height = len(content) * (FONT_SIZE + 10) + len(questions) * 3 * (FONT_SIZE + 10)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True
                if event.button == 4:
                    scroll_y = min(scroll_y + SCROLL_SPEED, 0)
                elif event.button == 5:
                    scroll_y = max(scroll_y - SCROLL_SPEED, -content_height + WINDOW_HEIGHT)

        screen.fill(BG_COLOR)

        y = scroll_y
        for line in content:
            text_surface = font.render(line, True, (0, 0, 0))
            screen.blit(text_surface, (20, y))
            y += FONT_SIZE + 10

        for idx, question in enumerate(questions):
            text_surface = font.render(question["text"], True, (0, 0, 0))
            screen.blit(text_surface, (20, y))

            true_button = pygame.Rect(20, y + FONT_SIZE + 5, 100, FONT_SIZE + 10)
            false_button = pygame.Rect(130, y + FONT_SIZE + 5, 100, FONT_SIZE + 10)

            question["true_rect"] = true_button
            question["false_rect"] = false_button

            true_color = SELECTED_COLOR if user_answers[idx] == True else BUTTON_COLOR
            false_color = SELECTED_COLOR if user_answers[idx] == False else BUTTON_COLOR

            pygame.draw.rect(screen, true_color, true_button)
            pygame.draw.rect(screen, false_color, false_button)

            true_text, true_text_rect = render_button_text("True", font, true_button, font_hedings)
            false_text, false_text_rect = render_button_text("False", font, false_button, font_hedings)

            screen.blit(true_text, true_text_rect)
            screen.blit(false_text, false_text_rect)

            if true_button.collidepoint(mouse_pos) and mouse_click[0]:
                user_answers[idx] = True
            if false_button.collidepoint(mouse_pos) and mouse_click[0]:
                user_answers[idx] = False

            y += 3 * (FONT_SIZE + 10)

        check_button = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 50, 100, 40)
        if check_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, check_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, check_button)
        check_text, check_text_rect = render_button_text("Check", font, check_button, font_hedings)
        screen.blit(check_text, check_text_rect)

        if check_button.collidepoint(mouse_pos) and button_released:
            for idx, question in enumerate(questions):
                if user_answers[idx] == question["answer"]:
                    print(f"{question['text']} - Correct")
                else:
                    print(f"{question['text']} - Incorrect")

        exit_button = pygame.Rect(20, WINDOW_HEIGHT - 50, 100, 40)
        if exit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, EXIT_HIGHLIGHT_COLOR, exit_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        exit_text, exit_text_rect = render_button_text("Exit", font, exit_button, font_hedings)
        screen.blit(exit_text, exit_text_rect)

        if exit_button.collidepoint(mouse_pos) and button_released:
            running = False

        pygame.display.flip()


def grammar_1_section():
    pygame.display.set_caption("Lesson 1 Grammar")
    global screen
    scroll_y = 0
    running = True

    grammar_questions = [
        {"sentence": "What is _____ doing?", "options": ["he", "they", "them"], "correct": "he"},
        {"sentence": "She _____ to the market yesterday.", "options": ["go", "gone", "went"], "correct": "went"},
        {"sentence": "The cat is _____ the tree.", "options": ["on", "in", "under"], "correct": "on"},
        {"sentence": "They _____ playing football.", "options": ["are", "is", "was"], "correct": "are"},
        {"sentence": "He _____ his homework already.", "options": ["did", "done", "does"], "correct": "did"},
        {"sentence": "Can you _____ me the book?", "options": ["gave", "give", "given"], "correct": "give"},
        {"sentence": "It _____ raining all day.", "options": ["has", "had", "is"], "correct": "has"},
        {"sentence": "I will _____ the cake tomorrow.", "options": ["make", "made", "makes"], "correct": "make"},
        {"sentence": "The children _____ in the park.", "options": ["play", "played", "playing"], "correct": "play"},
        {"sentence": "She _____ the movie last night.", "options": ["watch", "watches", "watched"],
         "correct": "watched"},
    ]

    selected_options = {i: None for i in range(len(grammar_questions))}
    question_height = len(grammar_questions) * (FONT_SIZE * 4)
    active_option = None

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True
                if event.button == 4:
                    scroll_y = min(scroll_y + SCROLL_SPEED, 0)
                elif event.button == 5:
                    scroll_y = max(scroll_y - SCROLL_SPEED, -question_height + WINDOW_HEIGHT)

                for i, (sentence, option_rects) in enumerate(option_boxes):
                    for j, rect in enumerate(option_rects):
                        if rect.collidepoint(mouse_pos):
                            selected_options[i] = j

        screen.fill(BG_COLOR)

        y = scroll_y
        option_boxes = []

        for i, question in enumerate(grammar_questions):

            sentence_surface = font.render(question["sentence"], True, (0, 0, 0))
            screen.blit(sentence_surface, (20, y))

            y += FONT_SIZE + 10
            option_rects = []
            for j, option in enumerate(question["options"]):
                option_rect = pygame.Rect(20 + j * 200, y, 150, FONT_SIZE + 10)
                color = SELECTED_COLOR if selected_options[i] == j else (200, 200, 200)
                pygame.draw.rect(screen, color, option_rect)

                option_surface = font.render(option, True, (0, 0, 0))
                screen.blit(option_surface, (option_rect.x + 5, option_rect.y + 5))

                option_rects.append(option_rect)

            option_boxes.append((question["sentence"], option_rects))
            y += FONT_SIZE + 20

        check_button = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 50, 100, 40)
        if check_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, check_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, check_button)
        check_text, check_text_rect = render_button_text("Check", font, check_button, font_hedings)
        screen.blit(check_text, check_text_rect)

        exit_button = pygame.Rect(20, WINDOW_HEIGHT - 50, 100, 40)
        if exit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, EXIT_HIGHLIGHT_COLOR, exit_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        exit_text, exit_text_rect = render_button_text("Exit", font, exit_button, font_hedings)
        screen.blit(exit_text, exit_text_rect)

        if exit_button.collidepoint(mouse_pos) and button_released:
            running = False

        if check_button.collidepoint(mouse_pos) and button_released:
            for i, question in enumerate(grammar_questions):
                selected = selected_options[i]
                if selected is not None:
                    selected_text = question["options"][selected]
                    if selected_text == question["correct"]:
                        print(f"Question {i + 1}: Correct")
                    else:
                        print(f"Question {i + 1}: Incorrect")
                else:
                    print(f"Question {i + 1}: No option selected")

        pygame.display.flip()


def lesson_2_menu():
    pygame.display.set_caption("Lesson 2")
    global screen
    lesson_running = True
    while lesson_running:
        mouse_pos = pygame.mouse.get_pos()
        button_pressed = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                lesson_running = False

            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()


            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True

        screen.fill(BG_COLOR)

        button_width = int(WINDOW_WIDTH * BUTTON_WIDTH_RATIO)
        button_height = int(WINDOW_HEIGHT * BUTTON_HEIGHT_RATIO)
        button_spacing = int(WINDOW_HEIGHT * BUTTON_SPACING_RATIO)

        lesson_buttons = {
            "LESSON 2": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 4 * button_height - button_spacing),
            "Vocabulary": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 1.5 * button_height - button_spacing),
            "Reading": (WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 - 0.5 * button_height),
            "Grammar": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 0.5 * button_height + button_spacing),
            "Exit": (
                WINDOW_WIDTH // 2 - button_width // 2, WINDOW_HEIGHT // 2 + 1.5 * button_height + 2 * button_spacing)
        }

        for button_text, position in lesson_buttons.items():
            button_rect = pygame.Rect(position[0], position[1], button_width, button_height)
            is_hovered = button_rect.collidepoint(mouse_pos)

            draw_button(screen, button_text, font, button_rect, is_hovered)

            if is_hovered and button_released:
                if button_text == "Exit":
                    lesson_running = False

                elif button_text == "Reading":
                    print("Reading 2 clicked")
                    reading_2_section()
                    pygame.display.set_caption("Lesson 2")

                elif button_text == "Vocabulary":
                    print("Vocabulary 2 clicked")
                    vocabulary_2_section()
                    pygame.display.set_caption("Lesson 2")

                elif button_text == "Grammar":
                    print("Grammar 2 clicked")
                    grammar_2_section()
                    pygame.display.set_caption("Lesson 2")

                else:
                    print(f"{button_text} clicked in Lesson 2!")

        pygame.display.flip()


def vocabulary_2_section():
    pygame.display.set_caption("Lesson 2 Vocabulary")
    global screen
    scroll_y = 0
    running = True

    user_inputs = {word: "" for word in VOCABULARY_1}
    vocab_height = len(VOCABULARY_1) * (FONT_SIZE + 20)
    active_input = None

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True
                elif event.button == 4:
                    scroll_y = min(scroll_y + SCROLL_SPEED, 0)
                elif event.button == 5:
                    scroll_y = max(scroll_y - SCROLL_SPEED, -vocab_height + WINDOW_HEIGHT)

                for word, input_rect in input_boxes:
                    if input_rect.collidepoint(mouse_pos):
                        active_input = word
                        break
                else:
                    active_input = None



            elif event.type == KEYDOWN and active_input is not None:
                if event.key == K_BACKSPACE:
                    user_inputs[active_input] = user_inputs[active_input][:-1]
                else:
                    user_inputs[active_input] += event.unicode

        screen.fill(BG_COLOR)

        y = scroll_y
        input_boxes = []

        for word in VOCABULARY_1:
            word_surface = font.render(word, True, (0, 0, 0))
            screen.blit(word_surface, (20, y))

            input_rect = pygame.Rect(200, y, 200, FONT_SIZE + 10)
            pygame.draw.rect(
                screen,
                (255, 255, 0) if active_input == word else (200, 200, 200),
                input_rect,
            )

            input_text_surface = font.render(user_inputs[word], True, (0, 0, 0))
            screen.blit(input_text_surface, (input_rect.x + 5, input_rect.y + 5))

            input_boxes.append((word, input_rect))
            y += FONT_SIZE + 20

        check_button = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 50, 100, 40)
        if check_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, check_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, check_button)
        check_text, check_text_rect = render_button_text("Check", font, check_button, font_hedings)
        screen.blit(check_text, check_text_rect)

        exit_button = pygame.Rect(20, WINDOW_HEIGHT - 50, 100, 40)
        if exit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, EXIT_HIGHLIGHT_COLOR, exit_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        exit_text, exit_text_rect = render_button_text("Exit", font, exit_button, font_hedings)
        screen.blit(exit_text, exit_text_rect)

        if exit_button.collidepoint(mouse_pos) and button_released:
            running = False

        if check_button.collidepoint(mouse_pos) and button_released:
            for word, correct_translation in VOCABULARY_1.items():
                if user_inputs[word].strip().lower() == correct_translation:
                    print(f"{word}: Correct")
                else:
                    print(f"{word}: Incorrect")

        pygame.display.flip()


def reading_2_section():
    pygame.display.set_caption("Lesson 2 Reading")
    global screen  # Use the global screen variable
    scroll_y = 0
    running = True

    content = [
        "This is a sample text for the reading section.",
        "You can add multiple lines to test the scrollable feature.",
        "Each line of text can represent a paragraph in your lesson.",
        "Feel free to expand this to fit your requirements.",
        "Scroll down to see more content.",
    ]

    questions = [
        {"text": "Question 1: Is this a sample question?", "true_rect": None, "false_rect": None, "answer": True},
        {"text": "Question 2: Does scrolling work?", "true_rect": None, "false_rect": None, "answer": True},
        {"text": "Question 3: Is this section interactive?", "true_rect": None, "false_rect": None, "answer": True},
    ]

    user_answers = [None] * len(questions)
    content_height = len(content) * (FONT_SIZE + 10) + len(questions) * 3 * (FONT_SIZE + 10)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True
                if event.button == 4:
                    scroll_y = min(scroll_y + SCROLL_SPEED, 0)
                elif event.button == 5:
                    scroll_y = max(scroll_y - SCROLL_SPEED, -content_height + WINDOW_HEIGHT)

        screen.fill(BG_COLOR)

        y = scroll_y
        for line in content:
            text_surface = font.render(line, True, (0, 0, 0))
            screen.blit(text_surface, (20, y))
            y += FONT_SIZE + 10

        for idx, question in enumerate(questions):
            text_surface = font.render(question["text"], True, (0, 0, 0))
            screen.blit(text_surface, (20, y))

            true_button = pygame.Rect(20, y + FONT_SIZE + 5, 100, FONT_SIZE + 10)
            false_button = pygame.Rect(130, y + FONT_SIZE + 5, 100, FONT_SIZE + 10)

            question["true_rect"] = true_button
            question["false_rect"] = false_button

            true_color = SELECTED_COLOR if user_answers[idx] == True else BUTTON_COLOR
            false_color = SELECTED_COLOR if user_answers[idx] == False else BUTTON_COLOR

            pygame.draw.rect(screen, true_color, true_button)
            pygame.draw.rect(screen, false_color, false_button)

            true_text, true_text_rect = render_button_text("True", font, true_button, font_hedings)
            false_text, false_text_rect = render_button_text("False", font, false_button, font_hedings)

            screen.blit(true_text, true_text_rect)
            screen.blit(false_text, false_text_rect)

            if true_button.collidepoint(mouse_pos) and mouse_click[0]:
                user_answers[idx] = True
            if false_button.collidepoint(mouse_pos) and mouse_click[0]:
                user_answers[idx] = False

            y += 3 * (FONT_SIZE + 10)

        check_button = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 50, 100, 40)
        if check_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, check_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, check_button)
        check_text, check_text_rect = render_button_text("Check", font, check_button, font_hedings)
        screen.blit(check_text, check_text_rect)

        if check_button.collidepoint(mouse_pos) and button_released:
            for idx, question in enumerate(questions):
                if user_answers[idx] == question["answer"]:
                    print(f"{question['text']} - Correct")
                else:
                    print(f"{question['text']} - Incorrect")

        exit_button = pygame.Rect(20, WINDOW_HEIGHT - 50, 100, 40)
        if exit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, EXIT_HIGHLIGHT_COLOR, exit_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        exit_text, exit_text_rect = render_button_text("Exit", font, exit_button, font_hedings)
        screen.blit(exit_text, exit_text_rect)

        if exit_button.collidepoint(mouse_pos) and button_released:
            running = False

        pygame.display.flip()


def grammar_2_section():
    pygame.display.set_caption("Lesson 2 Grammar")
    global screen
    scroll_y = 0
    running = True

    grammar_questions = [
        {"sentence": "What is _____ doing?", "options": ["he", "they", "them"], "correct": "he"},
        {"sentence": "She _____ to the market yesterday.", "options": ["go", "gone", "went"], "correct": "went"},
        {"sentence": "The cat is _____ the tree.", "options": ["on", "in", "under"], "correct": "on"},
        {"sentence": "They _____ playing football.", "options": ["are", "is", "was"], "correct": "are"},
        {"sentence": "He _____ his homework already.", "options": ["did", "done", "does"], "correct": "did"},
        {"sentence": "Can you _____ me the book?", "options": ["gave", "give", "given"], "correct": "give"},
        {"sentence": "It _____ raining all day.", "options": ["has", "had", "is"], "correct": "has"},
        {"sentence": "I will _____ the cake tomorrow.", "options": ["make", "made", "makes"], "correct": "make"},
        {"sentence": "The children _____ in the park.", "options": ["play", "played", "playing"], "correct": "play"},
        {"sentence": "She _____ the movie last night.", "options": ["watch", "watches", "watched"],
         "correct": "watched"},
    ]

    selected_options = {i: None for i in range(len(grammar_questions))}
    question_height = len(grammar_questions) * (FONT_SIZE * 4)
    active_option = None

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        button_released = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), RESIZABLE)
                recalculate_buttons()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_released = True
                if event.button == 4:
                    scroll_y = min(scroll_y + SCROLL_SPEED, 0)
                elif event.button == 5:
                    scroll_y = max(scroll_y - SCROLL_SPEED, -question_height + WINDOW_HEIGHT)

                for i, (sentence, option_rects) in enumerate(option_boxes):
                    for j, rect in enumerate(option_rects):
                        if rect.collidepoint(mouse_pos):
                            selected_options[i] = j

        screen.fill(BG_COLOR)

        y = scroll_y
        option_boxes = []

        for i, question in enumerate(grammar_questions):

            sentence_surface = font.render(question["sentence"], True, (0, 0, 0))
            screen.blit(sentence_surface, (20, y))

            y += FONT_SIZE + 10
            option_rects = []
            for j, option in enumerate(question["options"]):
                option_rect = pygame.Rect(20 + j * 200, y, 150, FONT_SIZE + 10)
                color = SELECTED_COLOR if selected_options[i] == j else (200, 200, 200)
                pygame.draw.rect(screen, color, option_rect)

                option_surface = font.render(option, True, (0, 0, 0))
                screen.blit(option_surface, (option_rect.x + 5, option_rect.y + 5))

                option_rects.append(option_rect)

            option_boxes.append((question["sentence"], option_rects))
            y += FONT_SIZE + 20

        check_button = pygame.Rect(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 50, 100, 40)
        if check_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, check_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, check_button)
        check_text, check_text_rect = render_button_text("Check", font, check_button, font_hedings)
        screen.blit(check_text, check_text_rect)

        exit_button = pygame.Rect(20, WINDOW_HEIGHT - 50, 100, 40)
        if exit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, EXIT_HIGHLIGHT_COLOR, exit_button)
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
        exit_text, exit_text_rect = render_button_text("Exit", font, exit_button, font_hedings)
        screen.blit(exit_text, exit_text_rect)

        if exit_button.collidepoint(mouse_pos) and button_released:
            running = False

        if check_button.collidepoint(mouse_pos) and button_released:
            for i, question in enumerate(grammar_questions):
                selected = selected_options[i]
                if selected is not None:
                    selected_text = question["options"][selected]
                    if selected_text == question["correct"]:
                        print(f"Question {i + 1}: Correct")
                    else:
                        print(f"Question {i + 1}: Incorrect")
                else:
                    print(f"Question {i + 1}: No option selected")

        pygame.display.flip()


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


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                button_released = True

    screen.fill(BG_COLOR)

    for button_text, position in button_positions.items():
        button_rect = pygame.Rect(position[0], position[1], button_width, button_height)
        is_hovered = button_rect.collidepoint(mouse_pos)

        draw_button(screen, button_text, font, button_rect, is_hovered)

        if is_hovered and button_released:
            if button_text == "Lesson 1":
                print("Lesson 1 clicked")
                lesson_1_menu()
                pygame.display.set_caption("Main Menu")
            elif button_text == "Lesson 2":
                print("Lesson 2 clicked")
                lesson_2_menu()
                pygame.display.set_caption("Main Menu")
            elif button_text == "Exit":
                running = False

    pygame.display.flip()

pygame.quit()





















