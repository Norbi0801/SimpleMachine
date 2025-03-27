import os
import random

from cell import Cell
from instruction import Instruction
from memory import Memory


class SimpleMachine:
    """
    A simulator of a simple computing machine based on a reduced instruction set architecture (RISC).

    Components:
    - Memory (M): 100 cells of memory (by default), initialized to Cell instances.
    - Accumulator (A): Main register used for arithmetic operations.
    - Program Counter (PC): Stores the address of the current instruction.
    - Halt Flag (H): Indicates if the program should stop.
    - Negative Flag (N): Set when subtraction results in a negative value.

    The machine reads and executes instructions provided as a list of integer codes.
    Each instruction is matched by a condition and executed by a corresponding handler.
    """
    max_memory_size = int(os.getenv('MAX_MEMORY_SIZE', 100))
    accumulative_start_value = int(os.getenv('ACCUMULATIVE_START_VALUE', 0))
    program_counter_start_value = int(os.getenv('PROGRAM_COUNTER_START_VALUE', 0))

    instruction_list =[Instruction(mnemonic=instruction[0], on_condition=instruction[1], to_do=instruction[2]) for instruction in [
        ('ADD', lambda code: code // 100 == 1, lambda code, env: setattr(env, "A", env.A + env.M[code % 100])),
        ('SUB', lambda code: code // 100 == 2, lambda code, env: [setattr(env, "N", 1 if int(env.A) - int(env.M[code % 100]) < 0 else 0), setattr(env, "A", (env.A - env.M[code % 100]))]),
        ('STA', lambda code: code // 100 == 3, lambda code, env: env.M.__setitem__(code % 100, env.A)),
        ('LDA', lambda code: code // 100 == 5, lambda code, env: setattr(env, "A", env.M[code % 100])),
        ('BRA', lambda code: code // 100 == 6, lambda code, env: setattr(env, "PC", code % 100)),
        ('BRZ', lambda code: code // 100 == 7, lambda code, env: setattr(env, "PC", code % 100) if env.A == 0 else None),
        ('BRP', lambda code: code // 100 == 8, lambda code, env: setattr(env, "PC", code % 100) if env.N == 0 else None),
        ('INP', lambda code: code == 901, lambda code, env: setattr(env, "A", int(input()))),
        ('OUT', lambda code: code == 902, lambda code, env: print(env.A)),
        ('HLT', lambda code: code < 100, lambda code, env: setattr(env, 'H', 1))
    ]]

    def __init__(self, program):
        self.M = Memory(SimpleMachine.max_memory_size)
        self.A = Cell(SimpleMachine.accumulative_start_value)
        self.PC = Cell(SimpleMachine.program_counter_start_value, SimpleMachine.max_memory_size)
        self.H = 0
        self.N = random.choice([0, 1])

        for i, command in enumerate(program):
            self.M[i] = command

    def run(self):
        """
        Starts executing the program loaded into memory.
        """
        while not self.H:
            command = self.M[self.PC]
            self.PC += 1
            for instruction in SimpleMachine.instruction_list:
                instruction.run_on_condition(command, self)


