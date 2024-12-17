import aoc_helper

DAY = 17
YEAR = 2024


def parse_input(input_text):
    regs_text, prog_text = input_text.split("\n\n")
    regs = []
    for line in regs_text.split("\n"):
        regs.append(int(line.split()[-1]))
    prog = prog_text.split()[-1]
    prog = [int(num) for num in prog.split(",")]
    return regs, prog


class Computer:

    def __init__(self, regs, prog):
        self.prog = prog
        self.pointer = 0

        self.A = regs[0]
        self.B = regs[1]
        self.C = regs[2]

        self.output = list()

    def restart(self, regs):
        self.A = regs[0]
        self.B = regs[1]
        self.C = regs[2]

        self.pointer = 0

        self.output = list()

    def combo_operand(self, num):
        if num <= 3:
            return num
        if num == 4:
            return self.A
        if num == 5:
            return self.B
        if num == 6:
            return self.C
        else:
            raise ValueError(f"{num} is not a valid combo operand")

    def run(self):
        while self.pointer < len(self.prog):
            self.run_one_inst()

    def run_one_inst(self):
        inst = self.prog[self.pointer]
        op = self.prog[self.pointer + 1]
        match inst:
            case 0:
                self.adv(op)
            case 1:
                self.bxl(op)
            case 2:
                self.bst(op)
            case 3:
                self.jnz(op)
            case 4:
                self.bxc(op)
            case 5:
                self.out(op)
            case 6:
                self.bdv(op)
            case 7:
                self.cdv(op)
        self.pointer += 2

    def adv(self, op):
        combo_op = self.combo_operand(op)
        self.A = self.A // (2 ** combo_op)

    def bxl(self, op):
        self.B = self.B ^ op

    def bst(self, op):
        combo_op = self.combo_operand(op)
        self.B = combo_op % 8

    def jnz(self, op):
        if self.A != 0:
            self.pointer = op - 2

    def bxc(self, op):
        self.B = self.B ^ self.C

    def out(self, op):
        combo_op = self.combo_operand(op)
        self.output.append(combo_op % 8)

    def bdv(self, op):
        combo_op = self.combo_operand(op)
        self.B = self.A // (2 ** combo_op)

    def cdv(self, op):
        combo_op = self.combo_operand(op)
        self.C = self.A // (2 ** combo_op)

    def get_output(self):
        return ",".join([str(num) for num in self.output])



@aoc_helper.communicator(YEAR, DAY, 1)
def p1(input_text):
    regs, prog = parse_input(input_text)
    computer = Computer(regs, prog)
    computer.run()
    return computer.get_output()


@aoc_helper.communicator(YEAR, DAY, 2)
def p2(input_text):
    regs, prog = parse_input(input_text)
    computer = Computer(regs, prog)
    prev_a = [0]
    for i in range(1, len(prog)+1):
        next_a = []
        for a in prev_a:
            a <<= 3
            for num in range(8):
                new_a = a | num
                computer.restart([new_a, 0, 0])
                computer.run()
                if computer.output[0] == prog[-i]:
                    next_a.append(new_a)
        prev_a = next_a
    return min(prev_a)


if __name__ == "__main__":
    p1_res = p1()
    aoc_helper.print_results(p1_res, part=1)

    p2_res = p2()
    aoc_helper.print_results(p2_res, part=2)
