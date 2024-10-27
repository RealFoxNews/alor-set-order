from client import Api
from settings import (REFRESH_TOKEN, USERNAME, DELAY,
                      ORDER_DIRECTION, ORDER_TICKER,
                      ORDER_UNITS, ORDER_NANO, ORDER_QUANTITY)
import time


print(REFRESH_TOKEN, USERNAME)

# Создаем объект API используя Refresh токен и Аккаунт - username
alor = Api(REFRESH_TOKEN, USERNAME)
# Указываем биржу
alor.exchange = 'MOEX'
# Получение списка серверов для рынков: Валютный, Срочный, Фондовый,
# интересует значения 'portfolio'
print('\n Получение списка серверов для рынков')
print(alor.get_portfolios())
# Указываем рынок (portfolio для Фондового рынка)
alor.portfolio = 'D89790'
# Задержка в секундах между попытками
delay_seconds = float(DELAY)

# Функция, которую нужно выполнять до получения успешного результата
def execute_code(price: float):
    result = alor.set_limit_order(ticker=ORDER_TICKER,
                                  quantity=int(ORDER_QUANTITY),
                                  price=price,
                                  side=ORDER_DIRECTION
                                  )
    print('\n Установить лимитную заявку: купить {ORDER_QUANTITY} лотов {ORDER_TICKER}} по 290')
    print(result)
    return result

# Цикл, который выполняет код до тех пор, пока не получен результат {'message': 'success'}
price = float(str(ORDER_UNITS)+"."+str(ORDER_NANO))
while True:
    result = execute_code(price)
    if result and result.pop('message') == 'success':
        print('Лимитная заявка успешно установлена.')
        break
    else:
        print('Не удалось установить лимитную заявку. Повторная попытка через {} секунд...'.format(delay_seconds))
        time.sleep(delay_seconds)

# Запрос информации о всех заявках
print('\n Запрос информации о всех заявках')
print(alor.get_orders_info())
