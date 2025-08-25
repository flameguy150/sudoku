'''for music'''
import os
import sys
from src.neo.config import globals
import pygame


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def mute_music():
    '''
    should mute music if has volume
    should unmute music if has no volume
    use global flag 
    '''
    if globals.mute_flag == True:
        globals.SUDOKU_DJ.set_volume(0)
    elif globals.mute_flag == False:
        globals.SUDOKU_DJ.set_volume(0.7)

def display_w_h():
    custom_text = globals.cf_small.render(f"{globals.WIDTH} x {globals.HEIGHT}", True, (0, 0, 0)) # Green text

    globals.screen.blit(custom_text, (0,0)) 

def resize_font():
    normal = globals.WIDTH//25
    small = globals.WIDTH//30
    globals.custom_font = pygame.font.Font('assets/fonts/FSEX300.TTF', normal)
    globals.cf_small = pygame.font.Font('assets/fonts/FSEX300.TTF', small)