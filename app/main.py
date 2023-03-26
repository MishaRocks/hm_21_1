from app.store import Store
from app.shop import Shop
from app.request import Request
from app.exceptions import BaseError

store = Store({'печеньки': 16, 'собачки': 8, 'коробки': 11, 'котики': 12})
shop = Shop({'печеньки': 6, 'собачки': 2, 'коробки': 3, 'лемонад': 2})


def main():

    print(f'На {Request.destinations[0]} храниться: {store.get_items()}')
    print(f'На {Request.destinations[1]} храниться: {shop.get_items()}')

    while True:
        print('Введите запрос в формате: Доставить -количество- -наименование- из -пункт получения- в '
              '-пункт назначения-. Для остановки программы введите -Стоп-.')
        user_input = input()
        if user_input == 'Стоп':
            break
        try:
            task = Request(user_input)
            store.remove(task.product, task.quantity)
            print(f'Курьер забирает {task.quantity} {task.product} из {task.from_destination}')
            print(f'Курьер везет {task.quantity} {task.product} со {task.from_destination} в {task.to_destination}')

            shop.add(task.product, task.quantity)
            print(f'На {Request.destinations[0]} храниться: {store.get_items()}')
            print(f'На {Request.destinations[1]} храниться: {shop.get_items()}')

        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
