"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список,
второму — целое число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""
import yaml
from yaml.loader import SafeLoader

CONST = {
    'list': [],
    'int': 1,
    'dict': {
        '5_U+03D8': 'unicode',
        '2_€': 'unicode'
    }
}


def dumps_yaml(values: dict):
    with open('file.yaml', 'w', encoding='utf-8') as f:
        yaml_data = yaml.dump(
            data=values,
            default_flow_style=False,
            allow_unicode=True
        )
        f.write(yaml_data)

    with open('file.yaml', 'r', encoding='utf-8') as f:
        dict_data = yaml.load(f, Loader=SafeLoader)

    print(CONST == dict_data)


dumps_yaml(CONST)
