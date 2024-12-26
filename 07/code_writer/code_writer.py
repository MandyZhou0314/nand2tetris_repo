class CodeWriter:
    def __init__(self, file_name=""):
        self.file_name = file_name
        self.asm_codes = []
        self.jump_count = 0

    def clear(self):
        self.asm_codes = []

    def pop_stack_to_D(self):
        self.asm_codes.extend(["@SP", "M=M-1", "A=M", "D=M"])

    def push_D_to_stack(self):
        # fetch the value in D register and save to stack top
        self.asm_codes.extend(["@SP", "A=M", "M=D", "@SP", "M=M+1"])

    def save_D_to_R13(self):
        self.asm_codes.extend(["@R13", "M=D"])

    def write_arithmetic(self, arith: str) -> list:
        # split arith into three mappings
        # only one value included
        unary_ariths = {"not": "D=!D", "neg": "D=-D"}
        # with jump instruction
        jump_maps = {"gt": "JGT", "eq": "JEQ", "lt": "JLT"}
        # others
        binary_ariths = {"add": "D=D+M", "sub": "D=D-M",
                         "and": "D=D&M", "or": "D=D|M",
                         "gt": "D=D-M", "eq": "D=D-M", "lt": "D=D-M"}

        self.clear()
        self.pop_stack_to_D()  # pop x
        if arith in unary_ariths:
            self.asm_codes.append(unary_ariths[arith])
        elif arith in binary_ariths:
            self.save_D_to_R13()  # save x to r13
            self.pop_stack_to_D()  # pop y
            # calc with xy, save to D
            self.asm_codes.extend(["@R13", binary_ariths[arith]])
            if arith in jump_maps:
                self.asm_codes.extend([
                    f"@TRUE{self.jump_count}",
                    f"D;{jump_maps[arith]}",
                    "D=0",  # false case
                    f"@CONTINUE{self.jump_count}",
                    "0;JMP",
                    f"(TRUE{self.jump_count})",
                    "D=-1",
                    f"(CONTINUE{self.jump_count})"
                ])
                self.jump_count += 1
        self.push_D_to_stack()
        self.asm_codes[0] += f"  // {arith}"
        return self.asm_codes

    def write_push_pop(self, type, seg, i: int) -> list:
        self.clear()
        segment_dic = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT",
        }
        if type == "push":

            if seg in segment_dic:
                self.asm_codes = [
                    f"@{i}", "D=A", f"@{segment_dic[seg]}", "D=D+M",
                    "A=D", "D=M"
                ]
                self.push_D_to_stack()

            elif seg == "constant":
                self.asm_codes = [f"@{i}", "D=A"]  # addr = i
                self.push_D_to_stack()

            elif seg == "static":
                # SP=*filename.i
                self.asm_codes = [f"@{self.file_name}.{i}", "D=M"]
                self.push_D_to_stack()

            elif seg == "temp":
                self.asm_codes = [f"@{i+5}", "D=M"]  # addr = i+5
                self.push_D_to_stack()

            elif seg == "pointer":
                ptr_name = "THIS" if i == 0 else "THAT"
                # fetch value from this/that
                self.asm_codes = [f"@{ptr_name}", "D=M"]
                self.push_D_to_stack()

        else:
            # pop, no constant
            if seg in segment_dic:
                self.asm_codes = [
                    # cal addr
                    f"@{i}", "D=A", f"@{segment_dic[seg]}", "D=D+M",
                ]
                self.save_D_to_R13()
                self.pop_stack_to_D()
                self.asm_codes.extend(["@R13", "A=M", "M=D"])  # SP value to addr
                

            elif seg == "static":
                self.pop_stack_to_D()
                self.asm_codes.extend([f"@{self.file_name}.{i}", "M=D"])

            elif seg == "temp":
                self.pop_stack_to_D()
                self.asm_codes.extend([f"@{i+5}", "M=D"])  # fetch addr i+5 value

            elif seg == "pointer":
                ptr_name = "THIS" if i == 0 else "THAT"
                self.pop_stack_to_D()
                self.asm_codes.extend([f"@{ptr_name}", "M=D"])
        # debug
        self.asm_codes[0] += f"   // {type} {seg} {i}"
        return self.asm_codes
