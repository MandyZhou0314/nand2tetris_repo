from parser import Parser
from parser import InstructionType

def test_remove_wAndc():
    p = Parser()
    assert p.remove_wAndc("// this is a comment.") == ""
    assert p.remove_wAndc("do you know // this is a comment?") == "do you know"
    assert p.remove_wAndc(" ") == ""

def test_run_first_pass():
    raw_rows = [
        "// 123123",
        "A=A+1 // dsfdsfsdf",
        "  (LOOP) // dsfdsfdsf",
        "0;JUMP",
        "(END) //sdfsdf",
        "A=A+1"
    ]
    p = Parser(raw_rows)
    p.run_first_pass()
    assert len(p.first_pass_result) == 3
    assert p.symbol_table.get("LOOP") == 1
    assert p.first_pass_result[0] == "A=A+1"
    assert p.first_pass_result[1] == "0;JUMP"
    assert p.symbol_table.get("END") == 2
    
def test_run_second_pass_c():
    first_pass_result = [
        "A=A+1",
        "0;JMP",
        "M=D-1"
    ]
    p = Parser()
    p.first_pass_result = first_pass_result
    p.run_second_pass()
    assert len(p.second_pass_result[0]) == 16
    assert p.second_pass_result[0] == "1110110111100000"
    assert p.second_pass_result[1] == "1110101010000111"
    assert p.second_pass_result[2] == "1110001110001000"

def test_run_second_pass_a():
    first_pass_result = [
        "@1",
        "@2",
        "@sum",
        "@i",
        "@R0"
    ]
    p = Parser()
    p.first_pass_result = first_pass_result
    p.run_second_pass()
    assert len(p.second_pass_result[0]) == 16
    assert p.second_pass_result[0] == "0000000000000001"
    assert p.second_pass_result[1] == "0000000000000010"
    assert p.second_pass_result[2] == "0000000000010000"
    assert p.second_pass_result[3] == "0000000000010001"
    assert p.second_pass_result[4] == "0000000000000000"

def test_instructionType():
    p = Parser()
    p.current_instruction = "@123"
    assert p.instructionType() is InstructionType.A_INSTRUCTION
    p.current_instruction = "(LOOP)"
    assert p.instructionType() is InstructionType.L_INSTRUCTION
    p.current_instruction = "A=A+1"
    assert p.instructionType() is InstructionType.C_INSTRUCTION
    
    
def test_symbol():
    p = Parser()
    p.current_instruction = "@123"
    assert p.symbol() == "123"
    p.current_instruction = "@sum"
    assert p.symbol() == "sum"
    p.current_instruction = "(LOOP)"
    assert p.symbol() == "LOOP"
    
    
def test_dest():
    p = Parser()
    p.current_instruction = "A=A+1"
    assert p.dest() == "A"
    p.current_instruction = "D=A; JGT"
    assert p.dest() == "D"
    p.current_instruction = "D; JLT"
    assert p.dest() == "NULL"
    
    
def test_comp():
    p = Parser()
    p.current_instruction = "A=A+1"
    assert p.comp() == "A+1"
    p.current_instruction = "AM =D+1; JNE"
    assert p.comp() == "D+1"
    
    
def test_jump():
    p = Parser()
    p.current_instruction = "A;JGT"
    assert p.jump() == "JGT"
    p.current_instruction = "D= D; JGT"
    assert p.jump() == "JGT"
    p.current_instruction = "A"
    assert p.jump() == "NULL"