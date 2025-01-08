class CodeWriter:
    def __init__(self, file_name=""):
        self.file_name = file_name
        self.function_name = ""
        self.asm_codes = []
        self.jump_count = 0
        self.ret_i = 0

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
    
    def write_label(self, label: str):
        self.clear()
        self.asm_codes.extend([f"({self.file_name}.{self.function_name}${label})"])
        return self.asm_codes

    def write_goto(self, label: str):
        #unconditional jump
        self.clear()
        self.asm_codes.extend([f"@{self.file_name}.{self.function_name}${label}", "0;JMP"])
        return self.asm_codes
        
    def write_if(self, label: str):
        #conditional jump
        self.clear()
        #if cond is pop
        self.pop_stack_to_D()
        #jump if D is not equal to 0
        self.asm_codes.extend([f"@{self.file_name}.{self.function_name}${label}", "D;JNE"])
        return self.asm_codes
        
    def write_function(self, func: str, n_vars: int):
        self.clear()
        # write function label
        self.asm_codes.extend([f"({func})"])
        # initialize LCL variables "push constant 0; pop local 0"
        self.asm_codes.extend(["@0", "D=A"])
        for i in range(n_vars):
            self.push_D_to_stack()
        self.function_name = func
        return self.asm_codes
        
    def write_call(self, func, n_args: int):
        self.clear()
        return_label = f"{self.file_name}.{func}$ret.{self.ret_i}"
        self.asm_codes.extend(["// push retAddrLabel"])
        self.asm_codes.extend([f"@{return_label}", "D=A"])
        self.push_D_to_stack()
        
        self.asm_codes.extend(["// push LCL"])
        self.asm_codes.extend(["@LCL", "D=M"])
        self.push_D_to_stack()
        
        self.asm_codes.extend(["// push ARG"])
        self.asm_codes.extend(["@ARG", "D=M"])
        self.push_D_to_stack()
        
        self.asm_codes.extend(["// push THIS"])
        self.asm_codes.extend(["@THIS", "D=M"])
        self.push_D_to_stack()
                 
        self.asm_codes.extend(["// push THAT"])
        self.asm_codes.extend(["@THAT", "D=M"])
        self.push_D_to_stack()
        
        self.asm_codes.extend(["// ARG = SP – 5 – nArgs"])     
        self.asm_codes.extend(["@SP", "D=M", "@5", "D=D-A", f"@{n_args}", "D=D-A", "@ARG", "M=D"])
        
        self.asm_codes.extend(["// LCL = SP"])     
        self.asm_codes.extend(["@SP", "D=M", "@LCL", "M=D"])
        
        
        self.asm_codes.extend(["// goto functionName"])     
        self.asm_codes.extend([f"@{func}", "0;JMP"])
         
        # add (retAddrLabel): functionName$ret.i
        self.asm_codes.extend([f"({return_label})"])
        self.ret_i += 1
        return self.asm_codes
        
    def write_return(self):
        self.clear()
        self.asm_codes.extend(["// endFrame = LCL"])
        self.asm_codes.extend(["@LCL", "D=M", "@R14", "M=D"])        
        # Register name, offset
        def helper(register_name: str, offset: int) ->list:
            return [
                "@R14",
                "D=M",
                f"@{offset}",
                "D=D-A",
                "A=D",
                "D=M",
                f"@{register_name}",
                "M=D",
            ]
        self.asm_codes.extend(["// retAddr = *(endFrame–5)"])
        self.asm_codes.extend(helper("R15", 5))
        self.asm_codes.extend(["// *ARG = pop()"])
        self.pop_stack_to_D()
        self.asm_codes.extend(["@ARG", "A=M", "M=D"])
        self.asm_codes.extend(["// SP = ARG + 1"])   
        self.asm_codes.extend(["@ARG", "D=M+1", "@SP", "M=D"])                          
        self.asm_codes.extend(["// THAT = *(endFrame–1)"])
        self.asm_codes.extend(helper("THAT", 1))
        self.asm_codes.extend(["// THIS = *(endFrame–2)"])
        self.asm_codes.extend(helper("THIS", 2))
        self.asm_codes.extend(["// ARG = *(endFrame–3)"])
        self.asm_codes.extend(helper("ARG", 3))
        self.asm_codes.extend(["// LCL = *(endFrame–4)"])
        self.asm_codes.extend(helper("LCL", 4))
        self.asm_codes.extend(["// goto retAddr"])
        self.asm_codes.extend(["@R15", "A=M", "0;JMP"]) 
        return self.asm_codes