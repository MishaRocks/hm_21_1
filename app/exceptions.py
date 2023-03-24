class BaseError(Exception):
    message = 'Неизвестная ошибка'


class NotEnoughGoods(BaseError):
    message = 'Недостаточно товара'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места'


class UniqueGoodsOverLoad(BaseError):
    message = 'В магазине больше 5 уникальных товаров'


class NotRequiredGoods(BaseError):
    message = 'Запрошенный товар отсутствует'


class UnknownDestinationError(BaseError):
    message = 'Точкой отгрузки или выгрузки должны быть магазин или склад'
