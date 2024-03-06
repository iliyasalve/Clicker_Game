import os, sys
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from text_rendering import title_text, draw_score, draw_multipliers, draw_best_score
from image_placement import main_image_position, reset_button_position, buy_button_position
from manipulation_with_data import save_result, load_result

# window dimensions
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

# import all images
bg = pygame.image.load("img/bg.png")
cookie_img = pygame.image.load("img/cookie.png")
reset_img = pygame.image.load("img/reset.png")
reset_img_clicked = pygame.image.load("img/reset_clicked.png")
buy_img = pygame.image.load("img/buy.png")
buy_clicked_img = pygame.image.load("img/buy_clicked.png")

data_path = 'data/score.data'

# checking for the presence of a file with variables
if os.path.exists(data_path):
    score, multipliers, multipliers_cost, best_score = load_result(data_path)
else:
    score = 0
    multipliers = 1
    multipliers_cost = 5
    best_score = 0

# values for clicking on an image
click_timer = 0.01
click_timer_running = False
click_timer_initial_time = None

# pygame initialisation
pygame.init()

# creating a window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Clicker Game")
pygame.display.set_icon(cookie_img)

clock = pygame.time.Clock()

# placement of images
cookie, cookie_rect = main_image_position(cookie_img, 250, 250, WINDOW_WIDTH, WINDOW_HEIGHT)
cookie_clicked, cookie_clicked_rect = main_image_position(cookie_img, 265, 265, WINDOW_WIDTH, WINDOW_HEIGHT)

reset_button, reset_button_rect = reset_button_position(reset_img, 100, 60, WINDOW_WIDTH, WINDOW_HEIGHT)
reset_button_clicked, reset_button_clicked_rect = reset_button_position(reset_img_clicked, 100, 60, WINDOW_WIDTH, WINDOW_HEIGHT) 

buy_button, buy_button_rect = buy_button_position(buy_img, 100, 60, WINDOW_WIDTH, WINDOW_HEIGHT)
buy_button_clicked, buy_button_clicked_rect = buy_button_position(buy_clicked_img, 100, 60, WINDOW_WIDTH, WINDOW_HEIGHT) 


while True:
    # poll for events
    for event in pygame.event.get():

        # pygame.QUIT event means the user clicked X to close window
        if event.type == pygame.QUIT:

            if score > best_score:
                best_score = score

            save_result(data_path, score, multipliers, multipliers_cost, best_score)

            pygame.quit()
            sys.exit()

        # response to click
        if(event.type == pygame.MOUSEBUTTONDOWN):

            if(event.button == 1):

                # reaction to a click on an image with cookies
                if(cookie_rect.collidepoint(event.pos)):

                    click_timer_running = True
                    click_timer_initial_time = pygame.time.get_ticks() / 1000

                    score += multipliers

                    _, current_score = draw_score(score)
                
                # response to click on the "Reset" button
                elif (event.pos[0] >= reset_button_rect.x and event.pos[0] <= reset_button_rect.x + reset_button.get_width() and event.pos[1] >= reset_button_rect.y and event.pos[1] <= reset_button_rect.y + reset_button.get_height()):
                    
                    if score > best_score:
                        best_score = score
                        _, best_score_text = draw_best_score(best_score)

                    score = 0
                    multipliers = 1
                    multipliers_cost = 5

                    _, current_score = draw_score(score)
                    multipliers_title_text, multipliers_cost_text = draw_multipliers(multipliers, multipliers_cost)

                # response to click on the "Buy" button
                elif (event.pos[0] >= buy_button_rect.x and event.pos[0] <= buy_button_rect.x + buy_button.get_width() and event.pos[1] >= buy_button_rect.y and event.pos[1] <= buy_button_rect.y + buy_button.get_height()):
                    
                    if score >= multipliers_cost:

                        score -= multipliers_cost
                        multipliers += 1
                        multipliers_cost = multipliers_cost*2

                        _, current_score = draw_score(score)
                        multipliers_title_text, multipliers_cost_text = draw_multipliers(multipliers, multipliers_cost)
      
        # reaction to completing a click on the cookie image
        if(click_timer_running):

            if(pygame.time.get_ticks() / 1000 - click_timer_initial_time >= click_timer):
                click_timer_initial_time = None
                click_timer_running = False


    mouse_pos = pygame.mouse.get_pos()

    # drawing background
    screen.blit(bg, (0, 0))

    # drawing title
    screen.blit(title_text, title_text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//8)))    # title

    # drawing multipliers text
    multipliers_title_text, multipliers_cost_text = draw_multipliers(multipliers, multipliers_cost)
    screen.blit(multipliers_title_text, (round(0.045*WINDOW_WIDTH), WINDOW_HEIGHT // 2.5 ))
    screen.blit(multipliers_cost_text, (round(0.045*WINDOW_WIDTH), WINDOW_HEIGHT // 2.1 ))

    # drawing "Buy" button
    if (mouse_pos[0] >= buy_button_rect.x and mouse_pos[0] <= buy_button_rect.x + buy_button.get_width() and mouse_pos[1] >= buy_button_rect.y and mouse_pos[1] <= buy_button_rect.y + buy_button.get_height()):
        screen.blit(buy_button_clicked, buy_button_clicked_rect)
    else:
        screen.blit(buy_button, buy_button_rect)

    # drawing "Best score" text
    best_score_title, best_score_text = draw_best_score(best_score)
    screen.blit(best_score_title, best_score_title.get_rect(center=(WINDOW_WIDTH - WINDOW_WIDTH // 6.2, WINDOW_HEIGHT // 2.3 )))
    screen.blit(best_score_text, best_score_text.get_rect(center=(WINDOW_WIDTH - WINDOW_WIDTH // 6.2, WINDOW_HEIGHT // 1.975 )))

    # drawing reset button position
    if(mouse_pos[0] >= reset_button_rect.x and mouse_pos[0] <= reset_button_rect.x + reset_button.get_width() and mouse_pos[1] >= reset_button_rect.y and mouse_pos[1] <= reset_button_rect.y + reset_button.get_height()):
        screen.blit(reset_button_clicked, reset_button_clicked_rect)
    else:
        screen.blit(reset_button, reset_button_rect)

    # drawing score text
    score_title, current_score = draw_score(score)
    screen.blit(score_title, score_title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - (WINDOW_HEIGHT // 6))))
    screen.blit(current_score, current_score.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - (WINDOW_HEIGHT // 11))))

    # drawing main image (cookie) position
    if(not click_timer_running):
        screen.blit(cookie, cookie_rect)
    else:
        screen.blit(cookie_clicked, cookie_clicked_rect)

    # update() the display to put work on screen
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()