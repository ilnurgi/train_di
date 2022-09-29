"""информационное окно о программе
"""

__author__ = 'ilnurgi'

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput

from screens.sizes import MAIN_WINDOW_PADDING, TOP_BAR_HEIGHT, TOP_BAR_BTN_WIDTH, CONTENT_HEIGHT

_info_text = '''
Дневник тренировок.
Автор: Ильнур Гайфутдинов, ilnurgi
Telegram: @ilnurgi
'''


class InfoScreen(Screen):
    """информационное окно программы
    """

    def __init__(self):
        super().__init__()

        self.name = 'InfoScreen'

        self.top_layout = BoxLayout(
            orientation='vertical',
            padding=MAIN_WINDOW_PADDING,
        )
        self.add_widget(self.top_layout)

        self.__init__top_bar()
        self.__init__content()
        self.__init__bottom_bar()

    def __init__top_bar(self):
        """инициализация верхнего бара
        """
        top_bar = BoxLayout(
            orientation='horizontal',
            height=TOP_BAR_HEIGHT,
            size_hint_y=None,
        )
        top_bar_text = Label(
            text='О программе',
        )
        top_bar.add_widget(top_bar_text)
        self.top_layout.add_widget(top_bar)

    def __init__content(self):
        """инициализация виджетов контента
        """

        content_scroll_lt = StackLayout(
            size_hint_y=None,
            height=CONTENT_HEIGHT,
            padding=5,
        )
        content_scroll_lt.bind(
            minimum_height=content_scroll_lt.setter('height')
        )

        content_sv = ScrollView()
        content_sv.add_widget(content_scroll_lt)

        content_lt = StackLayout()
        content_lt.add_widget(content_sv)

        text_input = TextInput(
            text=_info_text,
            readonly=True,
        )
        content_scroll_lt.add_widget(text_input)

        self.top_layout.add_widget(content_lt)

    def __init__bottom_bar(self):
        """инициализация нижнего бара
        """
        bottom_bar = BoxLayout(
            orientation='horizontal',
            height=TOP_BAR_HEIGHT,
            size_hint_y=None,
        )
        bottom_bar_btn_return = Button(
            text='<-',
            width=TOP_BAR_BTN_WIDTH,
            size_hint_x=None,
            on_press=self.on_press_btn_return,
        )
        bottom_bar.add_widget(bottom_bar_btn_return)
        self.top_layout.add_widget(bottom_bar)

    def on_enter(self, *args):
        """отображение окна
        """
        self.manager.transition.direction = 'right'

    def on_press_btn_return(self, instance):
        """обработчик кнопки назад
        """
        self.manager.show_last_screen(direction='right')
