"""окно списка программ
"""

__author__ = 'ilnurgi'


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

from data.programs import get_programs
from screens.sizes import (
    MAIN_WINDOW_PADDING, TOP_BAR_HEIGHT, TOP_BAR_BTN_WIDTH, CONTENT_HEIGHT, CONTENT_ITEMS_HEIGHT, BOTTOM_BAR_HEIGHT,
    BOTTOM_BAR_BTN_WIDTH,
)

PROGRAMS_SCREEN_NAME = 'ProgramsScreen'


class ProgramsScreen(Screen):
    """окно списка программ
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.name = 'ProgramsScreen'

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
            text='Список программ',
        )
        top_bar_btn_add = Button(
            text='+',
            width=TOP_BAR_BTN_WIDTH,
            size_hint_x=None,
            on_press=self.create_program,
        )
        top_bar.add_widget(top_bar_text)
        top_bar.add_widget(top_bar_btn_add)
        self.top_layout.add_widget(top_bar)

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

        self.top_layout.add_widget(content_lt)

        programs = get_programs()
        self.empty_programs_label = Label(
            text='Программы не найдены'
        )
        if not programs:
            self.add_widget(self.empty_programs_label)
        else:
            for program in programs:
                content_scroll_lt.add_widget(
                    Button(
                        text=str(f'-{program.id}'),
                        height=CONTENT_ITEMS_HEIGHT,
                        size_hint_y=None,
                    )
                )

    def __init__bottom_bar(self):
        """инициализция нижнего бара меню
        """

        bottom_bar = BoxLayout(
            orientation='horizontal',
            height=BOTTOM_BAR_HEIGHT,
            size_hint_y=None,
        )
        bottom_bar_btn_settings = Button(
            text='P',
            width=BOTTOM_BAR_BTN_WIDTH,
            size_hint_x=None,
        )
        bottom_bar_btn_info = Button(
            text='i',
            width=BOTTOM_BAR_BTN_WIDTH,
            size_hint_x=None,
            on_press=self.show_info_screen,
        )

        bottom_bar.add_widget(bottom_bar_btn_settings)
        bottom_bar.add_widget(bottom_bar_btn_info)
        self.top_layout.add_widget(bottom_bar)

    def on_enter(self, *args):
        """отображение окна
        """
        self.manager.transition.direction = 'left'

    def show_info_screen(self, instance):
        """отображаем окно с информацией о программе
        """
        self.manager.show_info_screen()

    def create_program(self, instance):
        """созание новой программы
        """

        modal_view = ModalView(

            size=(400, 400),
            size_hint=(None, None),
        )
        modal_view.add_widget(
            Label(text='123'),
        )
        modal_view.open()