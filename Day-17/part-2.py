import re
from concurrent.futures import ProcessPoolExecutor


class ThreeBitComputer:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.instruction_pointer = 0
        self.output_register = []
        self.opcode_operations = {
            0: self._adv,
            1: self._bxl,
            2: self._bst,
            3: self._jnz,
            4: self._bxc,
            5: self._out,
            6: self._bdv,
            7: self._cdv,
        }

    def run(self, program):
        while self.instruction_pointer < len(program) - 1:
            opcode = program[self.instruction_pointer]
            operand = program[self.instruction_pointer + 1]
            operation = self.opcode_operations[opcode]
            operation(operand)

    def _adv(self, input) -> None:
        operand = self._get_operand(input, type="combo")
        self.A = int(self.A / (2**operand))
        self.instruction_pointer += 2

    def _bxl(self, input) -> None:
        operand = self._get_operand(input, type="literal")
        self.B = self.B ^ operand
        self.instruction_pointer += 2

    def _bst(self, input) -> None:
        operand = self._get_operand(input, type="combo")
        self.B = operand % 8
        self.instruction_pointer += 2

    def _jnz(self, input) -> None:
        operand = self._get_operand(input, type="literal")
        if self.A == 0:
            self.instruction_pointer += 2
            return
        self.instruction_pointer = operand

    def _bxc(self, input) -> None:
        self.B = self.B ^ self.C
        self.instruction_pointer += 2

    def _out(self, input) -> None:
        operand = self._get_operand(input, type="combo")
        self.output_register.append(operand % 8)
        self.instruction_pointer += 2

    def _bdv(self, input):
        operand = self._get_operand(input, type="combo")
        self.B = int(self.A / (2**operand))
        self.instruction_pointer += 2

    def _cdv(self, input):
        operand = self._get_operand(input, type="combo")
        self.C = int(self.A / (2**operand))
        self.instruction_pointer += 2

    def _get_operand(self, input, type):
        if type == "literal":
            return input

        if 0 <= input <= 3:
            return input

        if input == 4:
            return self.A

        if input == 5:
            return self.B

        if input == 6:
            return self.C

        raise Exception()


with open("input.txt") as f:
    A, B, C, program = re.findall(r": (\d+(?:,\d+)*)\b", f.read())
A, B, C = int(A), int(B), int(C)
program = list(map(int, program.split(",")))


def find(a, max_a):
    A = a
    max_a = a + 1_000_000
    while A != max_a:
        computer = ThreeBitComputer(A, B, C)
        computer.run(program)
        if computer.output_register == program:
            break
        A += 1
        print(A)


with ProcessPoolExecutor(max_workers=8) as e:
    f = []
    for i in range(1, 1_000_000_000, 1_000_000):
        fut = e.submit(find, i)
        f.append(fut)
    r = [k.result() for k in fut]
