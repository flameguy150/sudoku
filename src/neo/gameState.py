import pygame
from src.neo import globals
from src.neo.config import RED, TITLE_MENU_BG, WIDTH, HEIGHT


class gameStateManager:
    def __init__(self):
        pass

def main_menu():
        globals.screen.fill(TITLE_MENU_BG)

        # draw text
        custom_text = globals.custom_font.render("Welcome to Sudoku!", True, (100, 137, 150)) # Green text
        globals.screen.blit(custom_text, (WIDTH // 2 - custom_text.get_width() // 2, 100)) # Center the text horizontally
