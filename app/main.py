from app.store import Store
from app.shop import Shop
from app.request import Request
from app.exceptions import BaseError

store = Store({'печеньки': 16, 'собачки': 8, 'коробки': 11})
shop = Shop({'печеньки': 9, 'собачки': 2, 'коробки': 3, 'лемонад': 2})


def main():

    print(f'На {Request.destinations[0]} храниться: {store.get_items()}')
    print(f'На {Request.destinations[1]} храниться: {shop.get_items()}')
    print('Введите запрос в формате: Доставить -количество- -наименование- из -пункт получения- в '
          '-пункт назначения-. Для остановки программы введите -Стоп-.')
    user_input = input()
    task = Request(user_input)

    while True:
        if task == 'Стоп':
            break
        try:
            store.remove(task.product, task.quantity)
            print(f'Курьер забирает {task.quantity} {task.product} из {task.from_destination}')
            print(f'Курьер везет {task.quantity} {task.product} со {task.from_destination} в {task.to_destination}')

            shop.add(task.product, task.quantity)
            print(f'На {Request.destinations[0]} храниться: {store.get_items()}')
            print(f'На {Request.destinations[1]} храниться: {shop.get_items()}')

            break

        except BaseError as error:
            print(error.message)
            break


if __name__ == '__main__':
    main()
