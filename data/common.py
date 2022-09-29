"""общие методы для работы с базой
"""

import sqlite3

from typing import Union

__connection: Union[None, sqlite3.Connection] = None


def get_connection() -> sqlite3.Connection:
    """возвращает объект соединения с базой
    """
    global __connection
    if not __connection:
        __connection = sqlite3.connect('train_di.db')
        __connection.row_factory = sqlite3.Row
    return __connection


def close_connection():
    """закрываем соединение с базой
    """
    global __connection
    if not __connection:
        return
    __connection.close()


def update_database():
    """создает/обновляет базу
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''
        create table if not exists
        "Programs"
        (
          id int
        )
        '''
    )
    connection.commit()
