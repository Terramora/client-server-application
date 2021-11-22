"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
"""
import platform
from subprocess import Popen, PIPE

import chardet

URLS = ['yandex.ru', 'youtube.com']

OS_NAME = platform.system()


def ping(host: str, count: int) -> str:
    command = ['ping',
               '-n' if OS_NAME == 'Windows' else '-c',
               str(count), host]

    with Popen(command, stdout=PIPE) as proc:
        bytes_res = proc.stdout.read()

    encoding = chardet.detect(bytes_res)
    return bytes_res.decode(encoding['encoding'])


for url in URLS:
    print(ping(url, 5))
