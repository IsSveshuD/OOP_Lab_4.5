#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os.path
import logging
from datetime import datetime
from typing import List, Dict, Union, Optional

logging.basicConfig(filename='contacts.log', level=logging.INFO)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def add_contact(contacts: List[Dict[str, Union[str, int]]], family: str,
                name: str, number: int, born: str) -> \
        List[Dict[str, Union[str, int]]]:
    """
    Добавить данные о человеке
    """
    contacts.append(
        {
            "family": family,
            "name": name,
            "number": number,
            "born": born
        }
    )
    return contacts


def display_contact(contacts: List[Dict[str, Union[str, int]]]) -> None:
    """
    Отобразить список контактов
    """
    if contacts:
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 30,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^30} | {:^20} |'.format(
                "№",
                "Фамилия",
                "Имя",
                "Номер телефона",
                "Дата Рождения"
            )
        )
        print(line)

        for idx, contact in enumerate(contacts, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:<30} | {:>20} |'.format(
                    idx,
                    contact.get('family', ''),
                    contact.get('name', ''),
                    contact.get('number', 0),
                    contact.get('born', '')
                )
            )
        print(line)
    else:
        print("Список контктов пуст.")


def select_contact(contacts: List[Dict[str, Union[str, int]]],
                   period: str) -> List[Dict[str, Union[str, int]]]:
    """
    Выбрать контакт
    """
    result = []
    for contact in contacts:
        if contact.get('family') == period:
            result.append(contact)

    return result


def save_contacts(file_name: str,
                  contacts: List[Dict[str, Union[str, int]]]) -> None:
    """
    Сохранить все контакты в файл JSON.
    """
    try:
        path = os.path.join(BASE_DIR, file_name)
        with open(path, "w", encoding="utf-8") as fout:
            json.dump(contacts, fout, ensure_ascii=False, indent=4)
    except Exception as exc:
        logging.error(str(exc))


def load_contacts(file_name: str) -> List[Dict[str, Union[str, int]]]:
    """
    Загрузить все контакты из файла JSON.
    """
    try:
        path = os.path.join(BASE_DIR, file_name)
        with open(path, "r", encoding="utf-8") as fin:
            data = json.load(fin)
            if isinstance(data, list):
                return data
            else:
                logging.warning(f"Unexpected data format in {file_name}")
                return []
    except Exception as exc:
        logging.error(str(exc))
        return []


def main(command_line: Optional[List[str]] = None) -> None:
    """
    Создать родительский парсер для определения имени файла
    """
    file_parser = argparse.ArgumentParser(add_help=False)
    file_parser.add_argument(
        "filename",
        action="store",
        help="The data file name"
    )

    # Создать основной парсер командной строки.
    parser = argparse.ArgumentParser("contacts")
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(dest="command")

    # Создать субпарсер для добавления контакта.
    add = subparsers.add_parser(
        "add",
        parents=[file_parser],
        help="Add a new contact"
    )
    add.add_argument(
        "-f",
        "--family",
        action="store",
        required=True,
        help="The contact's family"
    )
    add.add_argument(
        "-na",
        "--name",
        action="store",
        required=True,
        help="The contact's name"
    )
    add.add_argument(
        "-n",
        "--number",
        action="store",
        type=int,
        required=True,
        help="The contact's number"
    )
    add.add_argument(
        "-b",
        "--born",
        action="store",
        required=True,
        help="The born"
    )

    _ = subparsers.add_parser(
        "display",
        parents=[file_parser],
        help="Display all contacts"
    )
    # Создать субпарсер для выбора контакта.
    select = subparsers.add_parser(
        "select",
        parents=[file_parser],
        help="Select the contacts"
    )
    select.add_argument(
        "-F",
        "--familys",
        action="store",
        help="The required family"
    )

    # Выполнить разбор аргументов командной строки.
    args = parser.parse_args(command_line)
    logging.info(f"[{datetime.now()}]: {str(args)}")
    # Загрузить все контакты в файл, если файл существует.
    is_dirty = False
    if os.path.exists(args.filename):
        contacts = load_contacts(args.filename)
        logging.info("Контакты загружены.")
    else:
        contacts = []

    """
    Добавить контакт
    """
    if args.command == "add":
        contacts = add_contact(
            contacts,
            args.family,
            args.name,
            args.number,
            args.born
        )
        is_dirty = True
        logging.info("Контакт добавлен.")

    # Отобразить все контакты
    elif args.command == "display":
        display_contact(contacts)
        logging.info("Отображен список контактов")

    # Выбрать требуемый контакт.
    elif args.command == "select":
        selected = select_contact(contacts, args.familys)
        display_contact(selected)
        logging.info(f"Выбран контакт: {args.family}")

    # Сохранить данные в файл, если список контактов был изменен.
    if is_dirty:
        try:
            save_contacts(args.filename, contacts)
            logging.info("Контакты сохранены.")
        except Exception as exc:
            logging.error(str(exc))

    return


if __name__ == "__main__":
    main()
