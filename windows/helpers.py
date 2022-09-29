"""хелперы для виджетов
"""

__author__ = 'ilnurgi'

from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.stacklayout import StackLayout


class BorderedMixin:

    def __init__(self, **kwargs):
        bordered = kwargs.pop('bordered', True)
        border_color = kwargs.pop('border_color', (1, 1, 1, 1))

        super().__init__(**kwargs)

        self.bordered = bordered
        self.border_color = border_color

    def on_size(self, instance, value):
        if not self.bordered:
            return

        with self.canvas:
            Color(*self.border_color)
            Line(
                width=2,
                rectangle=(self.x, self.y, self.width, self.height)
            )



class BorderedAnchorLayout(BorderedMixin, AnchorLayout):
    """контейнер с обводкой
    """

class BorderedBoxLayout(BoxLayout):
    """контейнер с обводкой
    """
    bordered = True
    border_color = (1, 1, 1, 1, 1)

    def __init__(self, **kwargs):
        bordered = kwargs.pop('bordered', self.bordered)
        border_color = kwargs.pop('border_color', self.border_color)

        super().__init__(**kwargs)

        self.bordered = bordered
        self.border_color = border_color

    def on_size(self, instance, value):
        print(instance, value)
        if not self.bordered or not self.canvas:
            return

        with self.canvas:
            Color(*self.border_color)
            Line(
                width=2,
                rectangle=(self.x, self.y, self.width, self.height)
            )


class BorderedStackLayout(StackLayout):
    """контейнер с обводкой
    """
    bordered = True
    border_color = (1, 1, 1, 1, 1)
    border_width = 2

    def __init__(self, **kwargs):
        bordered = kwargs.pop('bordered', self.bordered)
        border_color = kwargs.pop('border_color', self.border_color)
        border_width = kwargs.pop('border_width', self.border_width)

        super().__init__(**kwargs)

        self.bordered = bordered
        self.border_color = border_color
        self.border_width = border_width

    def on_size(self, instance, value):
        print(instance, value)
        if not self.bordered or not self.canvas:
            return

        with self.canvas:
            Color(*self.border_color)
            Line(
                width=self.border_width,
                rectangle=(self.x, self.y, self.width, self.height)
            )
