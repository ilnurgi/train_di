"""окно со списком программ
"""

__author__ = 'ilnurgi'

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

from screens.sizes import MAIN_WINDOW_PADDING, TOP_BAR_HEIGHT, TOP_BAR_BTN_WIDTH, CONTENT_HEIGHT, CONTENT_ITEMS_HEIGHT


class ProgramsWindow(BoxLayout):
    """окно со списком программ
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = MAIN_WINDOW_PADDING

        self.__init__top_bar()
        self.__init__content()

    def __init__top_bar(self):
        """инициализация верхнего бара
        """
        top_bar = BoxLayout(
            orientation='horizontal',
            height=TOP_BAR_HEIGHT,
            size_hint_y=None,
        )
        top_bar_text = Label(
            text='Дневник Тренировок',
        )
        top_bar_btn_add = Button(
            text='+',
            width=TOP_BAR_BTN_WIDTH,
            size_hint_x=None,
        )
        top_bar_btn_settings = Button(
            text='P',
            width=TOP_BAR_BTN_WIDTH,
            size_hint_x=None,
        )
        top_bar_btn_info = Button(
            text='i',
            width=TOP_BAR_BTN_WIDTH,
            size_hint_x=None,
        )

        top_bar.add_widget(top_bar_text)
        top_bar.add_widget(top_bar_btn_add)
        top_bar.add_widget(top_bar_btn_settings)
        top_bar.add_widget(top_bar_btn_info)
        self.add_widget(top_bar)

    def __init__content(self):
        """инициализация виджетов контента
        """

        content_scroll_lt = StackLayout(
            size_hint_y=None,
            height=CONTENT_HEIGHT,
            spacing=5,
        )
        content_scroll_lt.bind(
            minimum_height=content_scroll_lt.setter('height')
        )

        content_sv = ScrollView()
        content_sv.add_widget(content_scroll_lt)

        content_lt = StackLayout()
        content_lt.add_widget(content_sv)

        self.add_widget(content_lt)

        for i in range(30):
            content_scroll_lt.add_widget(Button(text=str(f'-{i}'), height=CONTENT_ITEMS_HEIGHT, size_hint_y=None))
