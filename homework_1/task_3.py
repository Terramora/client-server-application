"""
Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

WORDS = ['attribute', 'класс', 'функция', 'type']


def task_3(ls: list) -> None:
    """
    :param ls:
    :return:
    Word: "attribute"
    Bytes_word: b'attribute'
    type: <class 'bytes'>
    Word: "класс"
    Bytes_word: b'\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81'
    type: <class 'bytes'>
    Word: "функция"
    Bytes_word: b'\xd1\x84\xd1\x83\xd0\xbd\xd0\xba\xd1\x86\xd0\xb8\xd1\x8f'
    type: <class 'bytes'>
    Word: "type"
    Bytes_word: b'type'
    type: <class 'bytes'>
    """
    for word in ls:
        print(f'Word: "{word}"\nBytes_word: {word.encode("utf-8")}\ntype: {type(word.encode("utf-8"))}')


task_3(WORDS)
"""
Записать в байтовом типе возможно все слова.
Однако кириллицу нельзя преобразовать в байты путем добавления "b" к строке. Например: b'класс' или b'функция'
"""
