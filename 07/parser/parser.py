from enum import Enum


import sys
sys.path.insert(0, "../code_writer")
from code_writer import CodeWriter

class CommandType(Enum):
    Command_Arithmetic = 1
    Command_Push = 2
    Command_Pop = 3
    
    
class Parser:
    def __init__(self, raw_commands = [], file_name = ""):
        self.raw_commands = raw_commands # vm translator read the file and transfer the content to a list
        self.first_pass_result = [] # filled after first pass
        self.second_pass_result = [] # filled after second pass
        self.current_command = ""
        self.code_writer = CodeWriter(file_name)
    
    def run_first_pass(self):
        # remove all content after "//" and heading&trailing whitespace by calling strip
        for command in self.raw_commands:
            if "//" in command:
                command, _ = command.split("//")
            if len(command) == 0:
                continue
            self.first_pass_result.append(command.strip())
    
    def run_second_pass(self):
        # add list from codewriter to total list
        for command in self.first_pass_result:
            asm_codes = []
            self.current_command = command
            if self.CommandType() == CommandType.Command_Arithmetic:
                asm_codes = self.code_writer.write_arithmetic(self.arg1())                
            elif self.CommandType() in [CommandType.Command_Push, CommandType.Command_Pop]:
                asm_codes = self.code_writer.write_push_pop(self.arg0(), self.arg1(), self.arg2())
            self.second_pass_result.extend(asm_codes)    
            
    def get_asm_codes(self):
        return self.second_pass_result
                    
    def count_words(self, str) -> int:
        # count the number of word in one command
        words = str.split()
        return len(words)
            
    def CommandType(self) -> CommandType:
        # check command type based on current_command
        if self.count_words(self.current_command) == 1:
            return CommandType.Command_Arithmetic
        elif self.current_command.startswith("push"):
            return CommandType.Command_Push
        elif self.current_command.startswith("pop"):
            return CommandType.Command_Pop 
    
    def arg0(self) -> str:
        #return push/pop
        assert self.CommandType() in [CommandType.Command_Push, CommandType.Command_Pop]
        type, _, _ = self.current_command.split()
        return type
    
    def arg1(self) -> str:
        #for Arithmetic type, arg1 return current type, for push&pop, arg1 return memory segment
        if self.CommandType() == CommandType.Command_Arithmetic:
            return self.current_command
        elif self.CommandType() in [CommandType.Command_Push, CommandType.Command_Pop]:
            _, segment, _ = self.current_command.split()
            return segment
        
    def arg2(self) -> int:
        #only for push and pop command type, arg2 return i
        assert self.CommandType() in [CommandType.Command_Push, CommandType.Command_Pop]
        _, _, i = self.current_command.split()
        return int(i)