import json
import socket


class ClientSocket:

    def __init__(self):
        self.sock = None
        self.BUFFER_SIZE = 1024

    def create_socket(self, host: str = 'localhost', port: int = 7777) -> None:
        """
        Open socket
        :param host:
        :param port:
        :return:
        """
        self.sock = socket.socket()
        self.sock.connect((host, port))

    def get_requests(self) -> dict:
        """
        get and return messages in list
        :return:
        """
        data = b''
        try:
            tmp: bytes = self.sock.recv(self.BUFFER_SIZE)
            while tmp:
                data += tmp
                tmp = self.sock.recv(self.BUFFER_SIZE)
        except socket.error:
            pass

        return json.loads(data.decode('utf-8'))

    @staticmethod
    def serializations(message: dict) -> bytes:
        """
        convert dict to json and encode utf-8
        :param message:
        :return:
        """
        return json.dumps(message).encode('utf-8')

    def send_message(self, message: dict) -> None:
        message = self.serializations(message)

        self.sock.sendall(message)
