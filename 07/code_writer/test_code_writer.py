from code_writer import CodeWriter

def test_write_push_dic():
    cd = CodeWriter()
    assert cd.write_push_pop("push", "local", 3) == ["@3", "D=A", "@LCL", "D=D+M","A=D", "D=M", 
                                                 "@SP", "A=M", "M=D", "@SP", "M=M+1"]
    assert cd.write_push_pop("push", "this", 1024) == ["@1024", "D=A", "@THIS", "D=D+M","A=D", "D=M", 
                                                 "@SP", "A=M", "M=D", "@SP", "M=M+1"]
def test_write_push_con():
    cd = CodeWriter()
    assert cd.write_push_pop("push", "constant", 78) == ["@78", "D=A", "@SP", "A=M", "M=D", "@SP", "M=M+1"]
    
def test_write_push_static():
    cd = CodeWriter()
    cd.file_name = "BasicTest"
    assert cd.write_push_pop("push", "static", 36) == ["@BasicTest.36", "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"]
    
def test_write_push_temp():
    cd = CodeWriter()
    assert cd.write_push_pop("push", "temp", 32) == ["@32", "D=A+5", "@SP", "A=M", "M=D", "@SP", "M=M+1"]
    
def test_write_push_pointer():
    cd = CodeWriter()
    assert cd.write_push_pop("push", "pointer", 0) == ["@THIS", "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"]
    assert cd.write_push_pop("push", "pointer", 1) == ["@THAT", "D=M", "@SP", "A=M", "M=D", "@SP", "M=M+1"]
    

def test_write_pop_dic():
    cd = CodeWriter()
    assert cd.write_push_pop("pop", "local", 3) == ["@3", "D=A", "@LCL", "D=D+M","@R13", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R13", "A=M", "M=D"]
    
def test_write_pop_static():
    cd = CodeWriter()
    cd.file_name = "BasicTest"
    assert cd.write_push_pop("pop", "static", 36) == ["@SP", "M=M-1", "A=M", "D=M", "@BasicTest.36", "M=D"]
    
def test_write_pop_temp():
    cd = CodeWriter()
    assert cd.write_push_pop("pop", "temp", 32) == ["@32", "D=A+5", "@R13", "M=D", "@SP", "M=M-1", "A=M", "D=M", "@R13", "A=M", "M=D"]
    
def test_write_pop_pointer():
    cd = CodeWriter()
    assert cd.write_push_pop("pop", "pointer", 0) == ["@SP", "M=M-1", "A=M", "D=M", "@THIS", "M=D"]
    assert cd.write_push_pop("pop", "pointer", 1) == ["@SP", "M=M-1", "A=M", "D=M", "@THAT", "M=D"]