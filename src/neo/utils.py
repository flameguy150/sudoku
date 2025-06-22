'''for music'''
import os
import sys
from src.neo import globals


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