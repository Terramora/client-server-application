"""
1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый 'отчетный' файл в формате CSV.
Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров 'Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'.
Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
'Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'. Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import os
from typing import Optional

import chardet


def write_to_csv(path: str = './result.csv') -> Optional[str]:
    data = get_data('.', '.txt')
    if data:
        with open(path, "w", newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(data[0])
            writer.writerows(list(zip(data[1], data[2], data[3])))

        return path

    return None


def open_and_decode_file(file_path: str) -> list:
    with open(file_path, 'rb+') as f:
        encoding = chardet.detect(f.read())['encoding']

    with open(file_path, 'r', encoding=encoding) as f:
        for row in f:
            ls = list((map(str.strip, row.split(':'))))

            yield ls


def get_listdir(path: str, extension: str) -> list:
    files = []
    for obj in os.listdir(path):
        if obj.endswith(extension):
            files.append(obj)
    return files


def get_data(path: str, extension: str) -> list:
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    os_prod_list, os_name_list, os_code_list, os_type_list = [[], [], [], []]
    files = get_listdir(path, extension)
    for file in files:
        for text in open_and_decode_file(os.path.join(path, file)):
            match text[0]:
                case 'Изготовитель системы':
                    os_prod_list.append(text[1])
                case 'Название ОС':
                    os_name_list.append(text[1])
                case 'Код продукта':
                    os_code_list.append(text[1])
                case 'Тип системы':
                    os_type_list.append(text[1])

    main_data.append(os_prod_list)
    main_data.append(os_name_list)
    main_data.append(os_code_list)
    main_data.append(os_type_list)

    return main_data


print(write_to_csv())
