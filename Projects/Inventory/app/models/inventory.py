from Projects.Inventory.app.utils.validators import validate_integer


class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer

        validate_integer('total', total, min_value=0)
        self._total = total

        validate_integer('allocated', allocated, 0, total,
                         custom_max_message='Allocated inventory cannot exceed total.')
        self._allocated = allocated

    @property
    def name(self):
        return self._name

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return str(self.__class__.name).lower()

    @property
    def available(self):
        return self._total - self._allocated

    def __str__(self):
        return f"Resource({self._name})"

    def __repr__(self):
        return f"{self.category}({self._name, self._manufacturer, self._total, self._allocated})"

    def claim(self, n):
        validate_integer('n', n, 1, self.available,
                         custom_max_message='Cannot claim more then available.')
        self._allocated += n

    def free_up(self, n):
        validate_integer('n', n, 1, self._allocated,
                         custom_max_message='Cannot return more then allocated.')
        self._allocated -= n

    def died(self, n):
        validate_integer('n', n, 1, self._allocated,
                         custom_max_message='Cannot return more then available.')
        self._total -= n
        self._allocated -= n

    def purchased(self, n):
        validate_integer('n', n, 1)
        self._total += n


class CPU(Resource):
    def __init__(self, name, manufacturer, total, allocated, cores, socket, power_watts):
        super().__init__(name, manufacturer, total, allocated)

        validate_integer('cores', cores, 1)
        validate_integer('power_watts', power_watts, 1)

        self._cores = cores
        self._socket = socket
        self._power_watts = power_watts

    @property
    def cores(self):
        return self._cores

    @property
    def socket(self):
        return self._socket

    @property
    def power_watts(self):
        return self._power_watts

    def __repr__(self):
        return f"{self.category}: {self.name} {self._socket} - {self._cores}"


class Storage(Resource):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb):
        super().__init__(name, manufacturer, total, allocated)

        validate_integer('capacity_gb', capacity_gb, 1)
        self._capacity_GB = capacity_gb

    @property
    def capacity_gb(self):
        return self._capacity_GB

    def __repr__(self):
        return f"{self.category}: {self._name} {self._capacity_GB} GB"


class HDD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, size, rpm):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)

        validate_integer('size', size, 1)
        validate_integer('rpm', rpm, 1_000, 50_000)
        self._size = size
        self._rpm = rpm

    @property
    def size(self):
        return self._size

    @property
    def rpm(self):
        return self._rpm

    def __repr__(self):
        s = super().__repr__()
        return f"{s}: {self._size}, {self._rpm} rpm"


class SSD(Storage):
    def __init__(self, name, manufacturer, total, allocated, capacity_gb, interface):
        super().__init__(name, manufacturer, total, allocated, capacity_gb)
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def __repr__(self):
        s = super().__repr__()
        return f"{s}: {self._interface}"
