import os


class Cell:
    """
    The Cell class represents a modular numeric container (e.g., an accumulator or register)
    with arithmetic operations bounded by a modulo value.

    The value is always kept within the range [0, p), where `p` is the modulus (default is 1000).
    """

    DEFAULT_P = int(os.getenv('CELL_THRESHOLD_VALUE', 1000))
    DEFAULT_VALUE = int(os.getenv('CELL_DEFAULT_VALUE', 0))

    def __init__(self, value=None, p=None):
        """
        Initialize a new Cell instance.

        :param value: Initial value of the cell. If None, uses DEFAULT_VALUE.
        :param p: Modulus to wrap the value around. If None, uses DEFAULT_P.
        """
        self.p = int(p) if p is not None else Cell.DEFAULT_P
        self._value = Cell.DEFAULT_VALUE if value is None else value % self.p

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val % self.p

    def __int__(self):
        return self._value

    def __repr__(self):
        return f"Cell({self._value})"

    def __add__(self, other):
        return (self._value + int(other)) % self.p

    def __sub__(self, other):
        return (self._value - int(other)) % self.p

    def __iadd__(self, other):
        self._value = (self._value + int(other)) % self.p
        return self

    def __isub__(self, other):
        self._value = (self._value - int(other)) % self.p
        return self

    def __eq__(self, other):
        return self._value == int(other)

    def __lt__(self, other):
        return self._value < int(other)

    def __le__(self, other):
        return self._value <= int(other)

    def __ge__(self, other):
        return self._value >= int(other)

    def __gt__(self, other):
        return self._value > int(other)

    def __index__(self):
        return self._value

