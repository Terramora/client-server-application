import os
import sys
from dataclasses import dataclass


@dataclass
class Client:
    ip: str
    port: int


@dataclass
class Server:
    ip: str
    port: int


@dataclass
class Config:
    client: Client
    server: Server


def get_argv() -> dict:
    result = {}
    args = sys.argv
    app = os.path.basename(args[0])
    if app == 'server.py':
        for i, arg in enumerate(args):
            try:
                if arg == '-a':
                    result['addr'] = args[i + 1]
                elif arg == '-p':
                    result['port'] = args[i + 1]
            except IndexError:
                print('Host or port not specified')
                sys.exit()

    elif app == 'client.py':
        try:
            result['addr'] = args[1]
            result['port'] = args[2]
        except IndexError:
            print('Host or port not specified')
            sys.exit()

    return result


def load_config():
    data = get_argv()

    return Config(
        client=Client(
            ip=data.get('addr', 'localhost'),
            port=int(data.get('port', 7777))
        ),
        server=Server(
            ip=data.get('addr', ''),
            port=int(data.get('port', 7777))
        )
    )
