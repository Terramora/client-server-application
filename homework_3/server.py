from homework_3.config import load_config
from homework_3.logger import get_logger
from task_1.server import ServerSocket

logger = get_logger('server')
config = load_config()

OK_RESPONSE = {
    'statusCode': 200,
    'description': 'OK',
    'body': {
        'details': 'Message received successfully'
    }
}

BAD_RESPONSE = {
    'statusCode': 500,
    'description': 'Internal Server Error',
    'body': {

    }
}

app = ServerSocket()
app.create_socket(
    host=config.server.ip,
    port=config.server.port
)

while True:
    app.accept_clients()
    if app.addr:
        addr_client = ":".join(map(str, app.addr))
        try:
            data = app.get_requests()
            logger.info(data)
            if data:
                message = app.serializations(OK_RESPONSE)
                action = data['action']
                logger.info('Message from: %s, message: %s' % (addr_client, data['body'][action]))
            else:
                message = app.serializations(BAD_RESPONSE)

            app.conn.sendall(message)

            app.conn.close()

        except ConnectionResetError:
            logger.error(f'Клиент: {addr_client} оборвал подключение.')
