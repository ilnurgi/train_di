"""размеры для виджетов
"""

__author__ = 'ilnurgi'

from kivy.core.window import Window
from kivy.utils import platform

if platform == 'linux':
    _resize = 3.5
    _window_height = 2340/_resize
    _window_width = 1080/_resize
    Window.size = (_window_width, _window_height)
else:
    _window_width, _window_height = Window.size

MAIN_WINDOW_PADDING = 10

TOP_BAR_HEIGHT = _window_height*0.07
TOP_BAR_BTN_WIDTH = _window_width*0.17

BOTTOM_BAR_HEIGHT = _window_height*0.07
BOTTOM_BAR_BTN_WIDTH = _window_width*0.17

CONTENT_HEIGHT = Window.height - MAIN_WINDOW_PADDING - TOP_BAR_HEIGHT - BOTTOM_BAR_HEIGHT
CONTENT_ITEMS_HEIGHT = CONTENT_HEIGHT * 0.1
