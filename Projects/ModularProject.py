class Mod:
    def __init__(self, value, modulus):
        if not isinstance(value, int) and not isinstance(modulus, int):
            raise ValueError('Args must be integers.')
        if modulus <= 0:
            raise ValueError('Modulus must be positive.')

        self._value = value % modulus
        self._modulus = modulus


    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def modulus(self):
        return self._modulus

    def __eq__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return self._value == other._value
        elif isinstance(other, int):
            return other % self._modulus == self._value
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Mod):
            return self._value < other._value
        elif isinstance(other, int):
            return self._value < other % self._modulus
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Mod):
            return self < other or self == other
        elif isinstance(other, int):
            return self < other or self == other
        return NotImplemented

    def __int__(self):
        return self._value

    def __hash__(self):
        return hash((self._value, self._modulus))

    def __neg__(self):
        return Mod(-self._value, self._modulus)

    def __repr__(self):
        return f"Mod(value={self._value}, modulus={self._modulus})"

    def __add__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return Mod(self._value + other._value, self._modulus)
        elif isinstance(other, int):
            return Mod(self._value + other, self._modulus)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return Mod(self._value - other._value, self._modulus)
        elif isinstance(other, int):
            return Mod(self._value - other, self._modulus)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return Mod(self._value * other._value, self._modulus)
        elif isinstance(other, int):
            return Mod(self._value * other, self._modulus)
        return NotImplemented

    def __pow__(self, power, modulo=None):
        if isinstance(power, Mod) and self._modulus == power._modulus:
            return Mod(self._value ** power._value, self._modulus)
        elif isinstance(power, int):
            return Mod(self._value ** (power % self._modulus), self._modulus)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            self._value = (self._value + other._value) % self._modulus
            return self
        elif isinstance(other, int):
            self._value = (self._value + other) % self._modulus
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            self._value = (self._value - other._value) % self._modulus
            return self
        elif isinstance(other, int):
            self._value = (self._value - other) % self._modulus
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            self._value = (self._value * other._value) % self._modulus
            return self
        elif isinstance(other, int):
            self._value = (self._value * other) % self._modulus
            return self
        return NotImplemented

    def __ipow__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            self._value = (self._value ** other._value) % self._modulus
            return self
        elif isinstance(other, int):
            self._value = (self._value ** (other % self._modulus)) % self._modulus
            return self
        return NotImplemented


p = Mod(8, 3)
p2 = Mod(8, 3)
print(p.value)
print(p == p2)
print(int(p))
print(p < 3)
print(p <= 2)
print(p <= p2)
print(id(p))
p += 5
print(id(p))
