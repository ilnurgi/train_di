"""Дневник тренировок
автор: Гайфутдинов Ильнур (ilnurgi)
"""

__author__ = 'ilnurgi'

from kivy.app import App

from data.common import close_connection, update_database

from screens.screen_manager import AppScreenManager


class TrainDiApp(App):
    """приложение Дневник тренировок
    """

    def build(self):
        """возвращает виджеты
        """
        return AppScreenManager()


update_database()
#update_program(Program())
TrainDiApp().run()
close_connection()
