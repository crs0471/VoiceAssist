import pyautogui as pg
from time import sleep

def volume_up(*args, **kwargs):
    for i in range(5):
        pg.press('volumeup')

def volume_down(*args, **kwargs):
    for i in range(5):
        pg.press('volumedown')

def mute(*args, **kwargs):
    print('mute: calling')
    pg.press('volumemute')

def media_play_pause(*args, **kwargs):
    pg.press('playpause')

def media_stop(*args, **kwargs):
    pg.press('stop')

def media_next(*args, **kwargs):
    pg.press('nexttrack')

def media_prev(*args, **kwargs):
    pg.press('prevtrack')