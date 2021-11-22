"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import chardet


WORDS = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'a+') as f:
    print(' '.join(WORDS), file=f)


with open('test_file.txt', 'rb') as f:
    encoding = chardet.detect(f.read())['encoding']
    print(encoding)


with open('test_file.txt', encoding='utf-8', errors='ignore') as f:
    print(f.read())

