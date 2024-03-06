import pygame

def main_image_position(img_name, img_x: int, img_y: int, WINDOW_WIDTH: int, WINDOW_HEIGHT: int):
    '''
    Returns an image adapted for working with pygame, as well as its coordinates
    '''

    img = pygame.transform.scale(img_name, (img_x, img_y)).convert_alpha()
    img_rect = img.get_rect()
    img_rect.x = WINDOW_WIDTH // 2 - img.get_width() // 2
    img_rect.y = WINDOW_HEIGHT // 2 - img.get_height() // 2
    
    return img, img_rect

def reset_button_position(img_name, img_x: int, img_y: int, WINDOW_WIDTH: int, WINDOW_HEIGHT: int):
    '''
    Returns an image adapted for working with pygame, as well as its coordinates
    '''

    img = pygame.transform.scale(img_name, (img_x, img_y)).convert_alpha()
    img_rect = img.get_rect()
    #img_rect.x = WINDOW_WIDTH - round(0.045*WINDOW_WIDTH) - img.get_width()
    #img_rect.y = WINDOW_HEIGHT // 2 - img.get_height() // 2
    #img_rect.x = WINDOW_WIDTH - round(0.112*WINDOW_WIDTH) - img.get_width()
    img_rect.x = WINDOW_WIDTH - round(0.1055*WINDOW_WIDTH) - img.get_width()
    img_rect.y = WINDOW_HEIGHT // 2 + img.get_height() // 2
    
    return img, img_rect


def buy_button_position(img_name, img_x: int, img_y: int, WINDOW_WIDTH: int, WINDOW_HEIGHT: int):
    '''
    Returns an image adapted for working with pygame, as well as its coordinates
    '''
    
    img = pygame.transform.scale(img_name, (img_x, img_y)).convert_alpha()
    img_rect = img.get_rect()
    #img_rect.x = round(0.045*WINDOW_WIDTH) - img.get_width() // 10
    #img_rect.y = WINDOW_HEIGHT // 2 
    img_rect.x = round(0.112*WINDOW_WIDTH) - img.get_width() // 10
    img_rect.y = WINDOW_HEIGHT // 2 + img.get_height() // 2
    
    return img, img_rect
