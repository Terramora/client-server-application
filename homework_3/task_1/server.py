import json
import socket
from typing import Optional


class ServerSocket:
    __slots__ = ('sock', 'conn', 'addr', 'BUFFER_SIZE')

    def __init__(self):
        self.sock = None
        self.conn = None
        self.addr = None
        self.BUFFER_SIZE = 1024

    def create_socket(self, host: str = '', port: int = 7777):
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen()

    def accept_clients(self) -> None:
        try:
            self.conn, self.addr = self.sock.accept()
        except socket.error as error:
            print(error)

    def get_requests(self) -> dict:
        """
        get and return messages in list
        :return:
        """
        self.conn.settimeout(5)
        data = b''
        try:
            tmp: bytes = self.conn.recv(self.BUFFER_SIZE)
            while tmp:
                data += tmp
                tmp = self.conn.recv(self.BUFFER_SIZE)
        except socket.error as error:
            pass

        return json.loads(data.decode('utf-8'))

    @staticmethod
    def serializations(message: dict) -> bytes:
        return json.dumps(message).encode('utf-8')
