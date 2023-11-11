class Mod:
    def __init__(self, value, modulus):
        if not isinstance(value, int) and not isinstance(modulus, int):
            raise ValueError('Args must be integers.')

        self._value = value

        if modulus <= 0:
            raise ValueError('Modulus must be positive.')
        self._modulus = modulus

        self._residue = value % modulus

    @property
    def value(self):
        return self._value

    @property
    def modulus(self):
        return self._modulus

    def __eq__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return self._residue == other._residue
        elif isinstance(other, int):
            return self._residue == other
        raise ValueError('Must be an integer.')

    def __gt__(self, other):
        if isinstance(other, Mod):
            return self._residue > other._residue
        elif isinstance(other, int):
            return self._residue > other
        raise ValueError('Must be an integer.')

    def __ge__(self, other):
        if isinstance(other, Mod):
            return self._residue > other._residue or self == other
        elif isinstance(other, int):
            return self._residue > other or self._residue == other
        raise ValueError('Must be an integer.')

    def __int__(self):
        return self._residue

    def __hash__(self):
        return hash((self._value, self._residue, self._modulus))

    def __repr__(self):
        return f"Mod(value={self._value}, modulus={self._modulus})"

    def __add__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return Mod(self._value + other._value, self._modulus)
        elif isinstance(other, int):
            return Mod(self._value + other, self._modulus)
        raise ValueError('Must be a Mod or integer.')

    def __sub__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return Mod(self._value - other._value, self._modulus)
        elif isinstance(other, int):
            return Mod(self._value - other, self._modulus)
        raise ValueError('Must be a Mod or integer.')

    def __mul__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            return Mod(self._value * other._value, self._modulus)
        elif isinstance(other, int):
            return Mod(self._value * other, self._modulus)
        raise ValueError('Must be a Mod or integer.')

    def __pow__(self, power, modulo=None):
        if isinstance(power, Mod) and self._modulus == power._modulus:
            return Mod(self._value ** power._value, self._modulus)
        elif isinstance(power, int):
            return Mod(self._value ** power, self._modulus)
        raise ValueError('Must be a Mod or integer.')

    def __isub__(self, other):
        if isinstance(other, Mod) and self._modulus == other._modulus:
            self._value += other._value
        elif isinstance(other, int):
            self._value = self._value + other
        raise ValueError('Must be a Mod or integer.')



p = Mod(8, 3)
p2 = Mod(8, 3)
print(p.value)
print(p == p2)
print(int(p))
print(p > 3)
print(p >= 2)
print(p <= p2)
print(id(p))
p += 5
print(id(p))
