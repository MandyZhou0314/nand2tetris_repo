from enum import Enum


import sys
sys.path.insert(0, "../code_writer")
from code_writer import CodeWriter

class CommandType(Enum):
    Command_Arithmetic = 1
    Command_Push = 2
    Command_Pop = 3
    Command_Label = 4
    Command_Goto = 5
    Command_If = 6
    Command_Function = 7
    Command_Return = 8
    Command_Call = 9
    
    
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
            command_type = self.CommandType()
            if command_type == CommandType.Command_Arithmetic:
                asm_codes = self.code_writer.write_arithmetic(self.arg1())                
            elif command_type in [CommandType.Command_Push, CommandType.Command_Pop]:
                asm_codes = self.code_writer.write_push_pop(self.arg0(), self.arg1(), self.arg2())
            elif command_type in [CommandType.Command_Label]:
                asm_codes = self.code_writer.write_label(self.arg1())
            elif command_type in [CommandType.Command_Goto]:
                asm_codes = self.code_writer.write_goto(self.arg1())
            elif command_type in [CommandType.Command_If]:
                asm_codes = self.code_writer.write_if(self.arg1())
            elif command_type in [CommandType.Command_Function]:
                asm_codes = self.code_writer.write_function(self.arg1(), self.arg2())
            elif command_type in [CommandType.Command_Return]:
                asm_codes = self.code_writer.write_return()
            elif command_type in [CommandType.Command_Call]:
                asm_codes = self.code_writer.write_call(self.arg1(), self.arg2())
            # write_call
            self.second_pass_result.extend(asm_codes)    
            
    def get_asm_codes(self):
        return self.second_pass_result
                    
    def count_words(self, str) -> int:
        # count the number of word in one command
        words = str.split()
        return len(words)
            
    def CommandType(self) -> CommandType:
        # check command type based on current_command
        if self.current_command.startswith("push"):
            return CommandType.Command_Push
        elif self.current_command.startswith("pop"):
            return CommandType.Command_Pop
        elif self.current_command.startswith("label"):
            return CommandType.Command_Label
        elif self.current_command.startswith("goto"):
            return CommandType.Command_Goto
        elif self.current_command.startswith("if-goto"):
            return CommandType.Command_If
        elif self.current_command.startswith("function"):
            return CommandType.Command_Function
        elif self.current_command.startswith("call"):
            return CommandType.Command_Call
        elif self.current_command.startswith("return"):
            return CommandType.Command_Return   
        elif self.count_words(self.current_command) == 1:
            return CommandType.Command_Arithmetic
    
    def arg0(self) -> str:
        #return push/pop, shouldn't be called when currend command is return
        assert self.CommandType() not in [CommandType.Command_Return]
        assert self.CommandType() in [CommandType.Command_Push, CommandType.Command_Pop, 
                                      CommandType.Command_Label, CommandType.Command_Goto, 
                                      CommandType.Command_If, CommandType.Command_Function, 
                                      CommandType.Command_Call, CommandType.Command_Return
                                      ]
        type = self.current_command.split()[0]
        return type
    
    def arg1(self) -> str:
        #for Arithmetic type, arg1 return current type, for push&pop, arg1 return memory segment
        if self.CommandType() == CommandType.Command_Arithmetic:
            return self.current_command
        elif self.CommandType() in [CommandType.Command_Push, CommandType.Command_Pop]:
            _, segment, _ = self.current_command.split()
            return segment
        elif self.CommandType() in [CommandType.Command_Label, CommandType.Command_Goto, CommandType.Command_If]:
            label= self.current_command.split()[1]
            return label
        elif self.CommandType() in [CommandType.Command_Function, CommandType.Command_Call]:
            _, function, _ = self.current_command.split()
            return function
        
        
    def arg2(self) -> int:
        #only for push and pop command type, arg2 return i
        assert self.CommandType() in [CommandType.Command_Push, CommandType.Command_Pop, CommandType.Command_Function, CommandType.Command_Call]
        _, _, i = self.current_command.split()
        return int(i)