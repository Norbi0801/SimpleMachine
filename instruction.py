from enum import Enum


class ExitInstructionCode(Enum):
    """
    Represents the result of attempting to execute an instruction.

    - DO: Indicates the instruction was executed.
    - NOT: Indicates the instruction condition did not match, so it was not executed.
    """
    DO = 1
    NOT = 0


class Instruction:
    """
    Represents a single instruction in the machine's instruction set.

    Each instruction has:
    - a mnemonic (e.g., 'ADD', 'SUB'),
    - a condition (`on_condition`) to determine if it should execute based on the code,
    - an action (`to_do`) that performs the instruction's behavior when the condition matches.
    """

    def __init__(self, mnemonic, on_condition, to_do):
        """
        Initialize the Instruction object.

        :param mnemonic: A string representing the instruction name.
        :param on_condition: A function that takes a numeric code and returns True if this instruction should run.
        :param to_do: A function that takes (code, environment) and performs the instruction's effect.
        """
        self.mnemonic = mnemonic
        self.on_condition = on_condition
        self.to_do = to_do

    def run_on_condition(self, code, environment):
        """
        Executes the instruction if the condition is met.

        :param code: The current instruction code (e.g., 520 for LDA 20).
        :param environment: The execution environment (e.g., machine context with registers and memory).
        :return: ExitInstructionCode.DO if executed, otherwise ExitInstructionCode.NOT
        """
        if self.on_condition(code):
            self.to_do(code, environment)
            return ExitInstructionCode.DO
        return ExitInstructionCode.NOT
