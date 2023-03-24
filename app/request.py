from app.exceptions import UnknownDestinationError


class Request:
    destinations = ['склад', 'магазин']

    def __init__(self, user_task):
        request_split = user_task.split(' ')

        self.quantity = int(request_split[1])
        self.product = request_split[2]
        self.from_destination = request_split[4]
        self.to_destination = request_split[6]

        if self.from_destination not in self.destinations or self.to_destination not in self.destinations:
            raise UnknownDestinationError
