"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

WORDS = ['администрирование', 'разработка', 'protocol', 'standard']


def task_4(ls: list) -> None:
    for word in ls:
        bytes_word = word.encode()
        decode_word = bytes_word.decode()

        print(f'Bytes: {bytes_word}\nString: {decode_word}')


task_4(WORDS)
