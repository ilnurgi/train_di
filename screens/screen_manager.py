"""менеджер окон приложений
"""

__author__ = 'ilnurgi'


from kivy.uix.screenmanager import ScreenManager

from screens.info import InfoScreen
from screens.programs import ProgramsScreen


class AppScreenManager(ScreenManager):
    """менеджер окон приложения
    """

    def __init__(self):
        super().__init__()

        self.programs_screen = ProgramsScreen()
        self.info_screen = InfoScreen()

        self.add_widget(self.programs_screen)
        self.add_widget(self.info_screen)

        self.last_show_screen = self.programs_screen.name

    def show_programs_screen(self):
        """отображаем окно сосписком программ
        """
        self.last_show_screen = self.current
        self.current = self.programs_screen.name

    def show_info_screen(self):
        """отображает информационное окно
        """
        self.last_show_screen = self.current
        self.current = self.info_screen.name

    def show_last_screen(self, direction=None):
        """отображаем последнее отображенное окно
        :param direction: направление анимации смены окна
        """
        self.current = self.last_show_screen
