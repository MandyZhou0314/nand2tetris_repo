from parser import Parser
from parser import CommandType

def test_run_first_pass():
    raw_commands = [
        "// add",
        "push constant 21 // dsfdsfsdf",
        "pop local 35 // dsfdsfdsf",
        "sub",
    ]
    p = Parser(raw_commands)
    p.run_first_pass()
    assert len(p.first_pass_result) == 3
    assert p.first_pass_result[0] == "push constant 21"
    assert p.first_pass_result[1] == "pop local 35"
    assert p.first_pass_result[2] == "sub"
    
def test_count_words():
    p = Parser()
    assert p.count_words("add") == 1
    assert p.count_words("push 1 local") == 3
    assert p.count_words("pop 3 static") == 3

def test_CommandType():
    p = Parser()
    p.current_command = "sub"
    assert p.CommandType() is CommandType.Command_Arithmetic
    p.current_command = "push 1054 local"
    assert p.CommandType() is CommandType.Command_Push
    p.current_command = "pop 32 static"
    assert p.CommandType() is CommandType.Command_Pop 
    
def test_arg1():
    p = Parser()
    p.current_command = "sub"
    assert p.arg1() == "sub"
    p.current_command = "add"
    assert p.arg1() == "add"
    p.current_command = "push local 1"
    assert p.arg1() == "local"
    p.current_command = "pop static 3"
    assert p.arg1() == "static"
    
def test_arg2():
    p = Parser()
    p.current_command = "push local 1"
    assert p.arg2() == 1
    p.current_command = "pop static 3"
    assert p.arg2() == 3