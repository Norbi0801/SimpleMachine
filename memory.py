from cell import Cell


class Memory:
    """
    Represents the memory component of the simple machine.

    The memory is implemented as a fixed-size list of `Cell` objects, each representing a memory cell.
    Supports standard indexing operations (get/set) using integer indices.

    Example:
        memory = Memory(100)
        memory[0] = Cell(42)
        value = memory[1]
    """
    def __init__(self, n, value=None, p=None):
        self._cell_list = [Cell(value, p) for _ in range(n)]

    def __getitem__(self, item):
        return self._cell_list[item]

    def __setitem__(self, key, value):
        self._cell_list[key] = value
