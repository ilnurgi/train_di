"""объекты для работа с программами тренировок
"""

__author__ = 'ilnurgi'

import sqlite3
from dataclasses import dataclass
from typing import List

from data.common import get_connection


@dataclass
class Program:
    """программа
    """
    id: int = None


def __program_from_db_row(db_row: sqlite3.Row) -> 'Program':
    """возвращает объект Program из записи бд
    :param db_row: запись из базы
    """
    dict_row = dict(db_row)
    return Program(
        id=dict_row['id']
    )


def get_programs() -> List[Program]:
    """возвращает список программ
    """
    cursor = get_connection().cursor()
    cursor.execute(
        '''
        select * from "Programs"
        '''
    )
    return [__program_from_db_row(program) for program in cursor]


def __create_program(program):
    """создает программу в базе
    :param program: программа
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        '''
        select id from "Programs"
        '''
    )
    exist_ids = [i[0] for i in cursor]
    if not exist_ids:
        create_id = 1
    else:
        min_id = min(exist_ids)
        max_id = max(exist_ids)
        for new_id in range(min_id, max_id+1):
            if new_id not in exist_ids:
                create_id = new_id
                break
        else:
            # вышли без брейк
            create_id = max_id + 1
    print(exist_ids, create_id)
    cursor.execute(
        '''
        insert into
        "Programs" (id)
        values (:id)
        ''',
        {
            'id': create_id,
        }
    )
    program.id = create_id

    connection.commit()


def update_program(program: Program):
    """создает/обновляет программу в БД
    :param program: программа
    """
    cursor = get_connection().cursor()
    if not program.id:
        __create_program(program)
    else:
        pass
