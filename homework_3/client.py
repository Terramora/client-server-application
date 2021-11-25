from homework_3.config import load_config
from homework_3.logger import get_logger
from task_1.client import ClientSocket

logger = get_logger('client')
config = load_config()

app = ClientSocket()
app.create_socket(
    host=config.client.ip,
    port=config.client.port
)

app.send_message(message={
    'action': 'message',
    'body': {
        'message': "It's message from client"
    }
})

data = app.get_requests()
if data:
    logger.info('Status: %s, answer: %s' % (data["description"], data["body"]["details"]))
