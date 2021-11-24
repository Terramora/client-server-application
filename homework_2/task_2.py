"""2. Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра."""
import datetime
import json
from json import JSONDecodeError


def write_order_to_json(item: str, quantity: int, price: float, buyer: str, date: datetime.date) -> None:
    if price < 0:
        print('Price must be > 0')

    with open('orders.json', encoding='utf-8') as f:
        old_data = f.read()

    with open('orders.json', 'w', encoding='utf-8') as json_file:
        values = {
            'item': item,
            'quantity': quantity,
            'price': price,
            'buyer': buyer,
            'date': str(date)
        }
        try:
            old_data = json.loads(old_data)
            old_data['orders'].append(values)
        except JSONDecodeError:
            old_data = {
                'orders': [values]
            }

        json.dump(old_data, json_file, ensure_ascii=False, indent=4)


write_order_to_json('test', 5, 10.5, '', datetime.date.today())
