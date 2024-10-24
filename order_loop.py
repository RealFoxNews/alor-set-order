from client import Api
from misc import print_orderbook
from settings import REFRESH_TOKEN, USERNAME
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
delay_seconds = 1

# Функция, которую нужно выполнять до получения успешного результата
def execute_code():
    result = alor.set_limit_order(ticker='VTBR', quantity=1, price=87.25, side='buy')
    print('\n Установить лимитную заявку: купить 5 лотов GAZP по 290')
    print(result)
    return result

# Цикл, который выполняет код до тех пор, пока не получен результат {'message': 'success'}
while True:
    result = execute_code()
    if result and result.pop('message') == 'success':
        print('Лимитная заявка успешно установлена.')
        break
    else:
        print('Не удалось установить лимитную заявку. Повторная попытка через {} секунд...'.format(delay_seconds))
        time.sleep(delay_seconds)

# Запрос информации о всех заявках
print('\n Запрос информации о всех заявках')
print(alor.get_orders_info())
