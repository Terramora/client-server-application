"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

BYTES_ARRAY = [b'class', b'function', b'method']  # Ручное приведение
ARRAY = ['class', 'function', 'method']


def task_2(ls: list) -> None:
    for word in ls:
        bytes_word = bytes(word, 'utf-8')  # Преобразование без методово класса str
        print(f'Word: {word}\nBytes_word: {bytes_word}\nlen: {len(bytes_word)}\ntype: {type(bytes_word)}')


def manual_task_2(ls: list) -> None:
    for word in ls:
        print(f'Bytes_word: {word}\nlen: {len(word)}\ntype: {type(word)}')


task_2(ARRAY)
manual_task_2(BYTES_ARRAY)
