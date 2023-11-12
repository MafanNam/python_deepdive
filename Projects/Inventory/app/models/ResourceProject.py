

class Resource:
    def __init__(self, name, manufacturer, total, allocated):
        self._name = name
        self._manufacturer = manufacturer
        self._total = total
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

    def __str__(self):
        return f"Resource({self._name})"

    def __repr__(self):
        return f"Resource({self._name, self._manufacturer, self._total, self._allocated})"

    def claim(self, n):
        if self._total < n:
            raise ValueError('n greater then total')
        self._total -= n
        self._allocated += n

    def freeup(self, n):
        if self._allocated < n:
            raise ValueError('n greater then allocated')
        self._total += n
        self._allocated -= n

    def died(self, n):
        if self._allocated < n or self._total < n:
            raise ValueError('n greater then allocated or total')
        self._total -= n
        self._allocated -= n

    def purchased(self, n):
        self._total += n

    @property
    def category(self):
        return str(self.__class__.name).lower()


















