import pygame

pygame.font.init()

# checks whether the computer has the given font
if pygame.font.match_font("georgia"):
    path = pygame.font.match_font("georgia")
else:
    path = None

# installing a custom font and its sizes
title_font = pygame.font.Font(path, 56)
text_font = pygame.font.Font(path, 30)
score_font = pygame.font.Font(path, 38)

# text rendering
title_text = title_font.render("Clicker Game", True, (248, 248, 217))

def draw_score(score: int):
    '''
    Returns rendered text regarding the current score to the screen
    '''

    score_title = score_font.render("Current Score", True, (248, 248, 217))
    current_score = score_font.render(f"{score}", True, (248, 248, 217))

    return score_title, current_score


def draw_multipliers(multipliers: int, multipliers_cost: int):
    '''
    Returns rendered text regarding the current multiplier and its cost to the screen
    '''

    multipliers_title_text = text_font.render(f"Multipliers: {multipliers}", True, (248, 248, 217))
    multipliers_cost_text = text_font.render(f"Multipliers cost: {multipliers_cost}", True, (248, 248, 217))

    return multipliers_title_text, multipliers_cost_text

def draw_best_score(best_score: int):
    '''
    Returns rendered text regarding the best score to the screen
    '''

    best_score_title = text_font.render(f"Best score: ", True, (248, 248, 217))
    best_score_text = text_font.render(f"{best_score}", True, (248, 248, 217))

    return best_score_title, best_score_text
